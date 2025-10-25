# 🇧🇷 Quick Start - Tradução para PT-BR

## ⚡ Tradução Rápida em 3 Passos

### 1️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Traduzir as receitas
```bash
python translate_recipes.py
```
Este processo traduzirá automaticamente todas as 13.000 receitas.
Tempo estimado: 2-4 horas (depende da conexão com internet)

### 3️⃣ Criar os bancos de dados
```bash
python rebuild_databases.py
```

## ✅ Resultado Final

Após executar os scripts, você terá:
- ✅ `13k-recipes-pt-br.csv` - CSV com todas as receitas em PT-BR
- ✅ `13k-recipes-pt-br.db` - Banco de dados completo em PT-BR  
- ✅ `5k-recipes-pt-br.db` - Banco de dados com 5k receitas em PT-BR

## 📝 Documentação já traduzida:
- ✅ README.md - em PT-BR
- ✅ metadata.json - em PT-BR

## 🔧 Requisitos Técnicos
- Python 3.7+
- Conexão com internet (para acessar Google Translate API)
- ~30 GB de espaço em disco (para arquivos temporários durante tradução)

## ❓ Precisa de ajuda?
Veja a documentação completa em [TRADUCAO.md](TRADUCAO.md)
