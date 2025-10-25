# Guia de Tradução do Dataset de Receitas

Este guia explica como traduzir todo o dataset de receitas para Português Brasileiro (PT-BR).

## Pré-requisitos

- Python 3.7 ou superior
- Conexão com a internet (necessária para a tradução)
- Bibliotecas Python necessárias

## Passo 1: Instalar Dependências

Instale as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install deep-translator pandas tqdm
```

## Passo 2: Traduzir o Arquivo CSV

Execute o script de tradução para traduzir as 13.000+ receitas do inglês para o português:

```bash
python translate_recipes.py
```

Este script irá:
- Ler o arquivo `13k-recipes.csv`
- Traduzir cada receita (Título, Ingredientes e Instruções) usando o Google Translate
- Salvar o resultado em `13k-recipes-pt-br.csv`
- Mostrar uma barra de progresso durante a tradução
- Salvar o progresso periodicamente (a cada 100 receitas)

**Observação:** Este processo pode demorar várias horas dependendo da velocidade da sua conexão com a internet. O script adiciona pequenos atrasos entre as requisições para evitar bloqueios por uso excessivo da API.

## Passo 3: Reconstruir os Arquivos de Banco de Dados

Depois que o CSV for traduzido, execute o script para recriar os arquivos de banco de dados SQLite:

```bash
python rebuild_databases.py
```

Este script irá:
- Ler o arquivo `13k-recipes-pt-br.csv`
- Criar `13k-recipes-pt-br.db` com todas as 13.000 receitas
- Criar `5k-recipes-pt-br.db` com as primeiras 5.000 receitas
- Preservar o esquema original do banco de dados

## Arquivos de Saída

Após executar ambos os scripts, você terá:

1. **13k-recipes-pt-br.csv** - Arquivo CSV com 13.000 receitas traduzidas (aproximadamente 26,6 MB)
2. **13k-recipes-pt-br.db** - Banco de dados SQLite com 13.000 receitas traduzidas (aproximadamente 26 MB)
3. **5k-recipes-pt-br.db** - Banco de dados SQLite com 5.000 receitas traduzidas (aproximadamente 9,9 MB)

## Arquivos de Documentação

Os seguintes arquivos de documentação já foram traduzidos para PT-BR:

- ✓ **README.md** - Documentação principal do repositório
- ✓ **metadata.json** - Metadados para Datasette
- **tutorial.md** - Permanece em inglês (referências técnicas a ferramentas em inglês)

## Solução de Problemas

### Erro de Conexão
Se você receber erros de conexão:
- Verifique sua conexão com a internet
- O Google Translate pode ter um limite de taxa. Aguarde alguns minutos e tente novamente
- O script salva o progresso periodicamente, então você pode retomar de onde parou

### Tradução de Baixa Qualidade
A tradução automática pode não ser perfeita. Para melhorar:
- Revise manualmente receitas importantes
- Considere usar serviços de tradução profissionais para maior precisão
- Mantenha os nomes próprios de pratos em suas línguas originais quando apropriado

### Arquivo CSV Não Encontrado
Certifique-se de estar executando os scripts no mesmo diretório que contém o arquivo `13k-recipes.csv`.

## Limitações

- A tradução automática usando Google Translate é gratuita mas tem limitações de taxa
- Nomes próprios de pratos podem não ser traduzidos corretamente
- Medidas e unidades podem precisar de ajustes para o padrão brasileiro
- Termos culinários técnicos podem necessitar de revisão manual

## Estrutura do Banco de Dados

As tabelas traduzidas mantêm o mesmo esquema:

```sql
CREATE TABLE "recipes" (
    [id] INTEGER PRIMARY KEY,
    [Title] TEXT,
    [Ingredients] TEXT,
    [Instructions] TEXT
);
```

## Licença

Este dataset traduzido mantém a licença original:
[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
