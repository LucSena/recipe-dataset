# Conjunto de dados de receitas gratuito, simples e aberto
Conjunto de dados simples de receitas com título do prato, ingredientes e instruções.

> **🇧🇷 Tradução PT-BR:** Veja [TRADUCAO.md](TRADUCAO.md) para instruções sobre como traduzir o dataset completo para Português Brasileiro.

### Tutorial
Siga o [tutorial](tutorial.md) para implementar busca semântica neste conjunto de dados usando Datasette

### 13k-recipes.csv
- Arquivo CSV com 13.000 receitas
- 26,6 mb

### 13k-recipes.db
- Arquivo de banco de dados com 13.000 receitas
- 26 mb

### 5k-recipes.db
- Arquivo de banco de dados com 5.000 receitas (as primeiras 5.000 linhas de 13k-recipes.db)
- 9,9 mb

## Fonte
O conjunto de dados original foi criado através de raspagem do site Epicurious. O conteúdo foi enviado para o Kaggle como [Food Ingredients and Recipes Dataset with Images](https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images). 


## Conteúdo
O conjunto de dados original tinha mais de 200 mb e continha 13.500 receitas e imagens. Removi as imagens e criei os recursos simplificados neste repositório. Nenhuma alteração foi feita no conteúdo textual.

Cada banco de dados contém uma tabela "recipes" com as seguintes três colunas:
- Title: Título do prato.
- Ingredients: Ingredientes conforme foram extraídos do site.
- Instructions: Instruções para recriar o prato.

### Esquema do banco de dados:
```
CREATE TABLE "recipes" (
    [id] INTEGER PRIMARY KEY,
    [Title] TEXT,
    [Ingredients] TEXT,
    [Instructions] TEXT
);
```

### Exemplo de linha:
| id | Title | Ingredients | Instructions |
| --- | --- | --- | --- |
| 29 | Baigan Chokha | ['2 large Italian eggplants', '1 tablespoon canola oil', '½ medium onion, chopped', '2 cloves garlic, finely chopped', '1 small tomato, chopped', '¼ teaspoon coarse salt, or to taste', 'Freshly ground black pepper to taste', '1 tablespoon coarsely chopped cilantro', 'Roti, for serving'] | Prepare a hot grill or preheat the broiler.<br>With a fork, pierce the eggplants all over, and place on the grill or under the broiler. Grill or broil until completely charred and soft, about 20 minutes, turning frequently (the eggplants will brown and blister quickly). Remove and allow to cool. <br>Once cool, cut open the eggplants and scrape out the flesh. The flesh should be soft to the touch and pulpy, and should easily come away from the skin. Set aside. <br>Heat the canola oil in a frying pan. Add the onion and sauté until translucent. Add the garlic and fry until the garlic turns a dark golden brown, then add the tomato and fry for 1 to 2 minutes.<br>Stir in the mashed eggplant and cook for about 2 minutes. Season with salt and black pepper to taste.<br>Garnish with the cilantro and serve with roti. |

## Licença:
[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)