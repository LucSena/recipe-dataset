#!/usr/bin/env python3
"""
Script to translate recipe dataset from English to Brazilian Portuguese (PT-BR)

This script translates the recipe CSV file using Google Translate API.
Requires internet connection to work.

Usage:
    python translate_recipes.py

Dependencies:
    pip install deep-translator pandas tqdm
"""

import csv
import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm
import time
import sys

# Configuration
INPUT_FILE = '13k-recipes.csv'
OUTPUT_FILE = '13k-recipes-pt-br.csv'
BATCH_SIZE = 100  # Process recipes in batches
DELAY = 1  # Delay between batches to avoid rate limiting

def translate_text(text, translator, max_retries=3):
    """
    Translate text with retry logic for handling API errors.
    
    Args:
        text: Text to translate
        translator: GoogleTranslator instance
        max_retries: Maximum number of retry attempts
    
    Returns:
        Translated text or original text if translation fails
    """
    if not text or pd.isna(text) or str(text).strip() == '':
        return text
    
    for attempt in range(max_retries):
        try:
            # Google Translate has a 5000 character limit per request
            if len(text) > 4500:
                # Split long text into chunks
                chunks = [text[i:i+4500] for i in range(0, len(text), 4500)]
                translated_chunks = []
                for chunk in chunks:
                    translated_chunk = translator.translate(chunk)
                    translated_chunks.append(translated_chunk)
                    time.sleep(0.5)  # Small delay between chunks
                return ' '.join(translated_chunks)
            else:
                return translator.translate(text)
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Translation error (attempt {attempt + 1}/{max_retries}): {e}")
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                print(f"Failed to translate after {max_retries} attempts: {text[:50]}...")
                return text  # Return original text if all retries fail
    
    return text

def translate_recipes(input_file, output_file):
    """
    Translate all recipes from English to Portuguese.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file
    """
    print(f"Loading recipes from {input_file}...")
    
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} recipes")
        
        # Check for required columns
        required_columns = ['Title', 'Ingredients', 'Instructions']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Error: Missing columns: {missing_columns}")
            print(f"Available columns: {list(df.columns)}")
            return
        
        # Initialize translator
        translator = GoogleTranslator(source='en', target='pt')
        
        # Create columns for translated content
        df['Title_PT'] = ''
        df['Ingredients_PT'] = ''
        df['Instructions_PT'] = ''
        
        # Translate recipes
        print("\nTranslating recipes to PT-BR...")
        print("This may take a while depending on the number of recipes and internet speed...\n")
        
        for idx, row in tqdm(df.iterrows(), total=len(df), desc="Translating"):
            # Translate Title
            df.at[idx, 'Title_PT'] = translate_text(row['Title'], translator)
            
            # Translate Ingredients
            df.at[idx, 'Ingredients_PT'] = translate_text(row['Ingredients'], translator)
            
            # Translate Instructions
            df.at[idx, 'Instructions_PT'] = translate_text(row['Instructions'], translator)
            
            # Add delay every BATCH_SIZE recipes to avoid rate limiting
            if (idx + 1) % BATCH_SIZE == 0:
                print(f"\nProcessed {idx + 1} recipes. Taking a short break...")
                time.sleep(DELAY)
                
                # Save intermediate progress
                df.to_csv(output_file, index=False)
                print(f"Progress saved to {output_file}")
        
        # Replace original columns with translated versions
        df['Title'] = df['Title_PT']
        df['Ingredients'] = df['Ingredients_PT']
        df['Instructions'] = df['Instructions_PT']
        
        # Drop temporary translation columns
        df = df.drop(columns=['Title_PT', 'Ingredients_PT', 'Instructions_PT'])
        
        # Save final translated dataset
        df.to_csv(output_file, index=False)
        print(f"\nTranslation complete! Saved to {output_file}")
        print(f"Total recipes translated: {len(df)}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """Main function to run the translation script."""
    print("=" * 60)
    print("Recipe Dataset Translation Script")
    print("English → Brazilian Portuguese (PT-BR)")
    print("=" * 60)
    print()
    
    # Check if input file exists
    import os
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file '{INPUT_FILE}' not found.")
        print("Please make sure the CSV file is in the same directory as this script.")
        sys.exit(1)
    
    # Confirm with user
    response = input(f"This will translate {INPUT_FILE} to Portuguese.\nContinue? (y/n): ")
    if response.lower() != 'y':
        print("Translation cancelled.")
        sys.exit(0)
    
    # Run translation
    translate_recipes(INPUT_FILE, OUTPUT_FILE)

if __name__ == '__main__':
    main()
