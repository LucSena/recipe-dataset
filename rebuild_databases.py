#!/usr/bin/env python3
"""
Script to rebuild SQLite database files from translated CSV

This script reads the translated CSV file and recreates the database files
with the Portuguese content.

Usage:
    python rebuild_databases.py

Dependencies:
    pip install pandas
"""

import sqlite3
import pandas as pd
import sys
import os

def create_database(csv_file, db_file, max_rows=None):
    """
    Create SQLite database from CSV file.
    
    Args:
        csv_file: Path to CSV file
        db_file: Path to output database file
        max_rows: Maximum number of rows to include (None for all rows)
    """
    print(f"\nCreating database: {db_file}")
    
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)
        
        if max_rows:
            df = df.head(max_rows)
            print(f"  Using first {max_rows} rows")
        else:
            print(f"  Using all {len(df)} rows")
        
        # Remove the old database if it exists
        if os.path.exists(db_file):
            os.remove(db_file)
            print(f"  Removed old database file")
        
        # Create connection to SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Create recipes table
        cursor.execute('''
            CREATE TABLE recipes (
                id INTEGER PRIMARY KEY,
                Title TEXT,
                Ingredients TEXT,
                Instructions TEXT
            )
        ''')
        
        # Insert data
        print(f"  Inserting {len(df)} recipes...")
        for idx, row in df.iterrows():
            # Skip the unnamed index column if it exists
            title = row.get('Title', '')
            ingredients = row.get('Ingredients', '')
            instructions = row.get('Instructions', '')
            
            cursor.execute('''
                INSERT INTO recipes (Title, Ingredients, Instructions)
                VALUES (?, ?, ?)
            ''', (title, ingredients, instructions))
        
        # Commit changes and close
        conn.commit()
        conn.close()
        
        # Get file size
        size_mb = os.path.getsize(db_file) / (1024 * 1024)
        print(f"  Database created successfully! Size: {size_mb:.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"  Error creating database: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function to rebuild database files."""
    print("=" * 60)
    print("Rebuild Database Files from Translated CSV")
    print("=" * 60)
    
    # Input and output files
    csv_file = '13k-recipes-pt-br.csv'
    
    # Check if translated CSV exists
    if not os.path.exists(csv_file):
        print(f"\nError: Translated CSV file '{csv_file}' not found.")
        print("Please run translate_recipes.py first to create the translated CSV.")
        sys.exit(1)
    
    print(f"\nInput CSV: {csv_file}")
    
    # Confirm with user
    response = input("\nThis will rebuild the database files. Continue? (y/n): ")
    if response.lower() != 'y':
        print("Operation cancelled.")
        sys.exit(0)
    
    # Create 13k database
    success_13k = create_database(csv_file, '13k-recipes-pt-br.db')
    
    # Create 5k database (first 5000 rows)
    success_5k = create_database(csv_file, '5k-recipes-pt-br.db', max_rows=5000)
    
    if success_13k and success_5k:
        print("\n" + "=" * 60)
        print("SUCCESS: All databases created successfully!")
        print("=" * 60)
        print("\nCreated files:")
        print("  - 13k-recipes-pt-br.db (complete dataset)")
        print("  - 5k-recipes-pt-br.db (first 5,000 recipes)")
    else:
        print("\nSome databases failed to create. Check the errors above.")
        sys.exit(1)

if __name__ == '__main__':
    main()
