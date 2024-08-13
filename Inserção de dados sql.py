import pandas as pd
import mysql.connector




# Alternativamente, substituir NaN por valores específicos
df = df.fillna({
    'PRODUTO': 'Unknown',  # Substitui NaN em 'PRODUTO' por 'Unknown'
    'MARCA': 'NoBrand',    # Substitui NaN em 'MARCA' por 'NoBrand'
    'MODELO': 'Unknown',   # Substitui NaN em 'MODELO' por 'Unknown'
    'DESCRICAO': '',       # Substitui NaN em 'DESCRICAO' por string vazia
    'PRATELEIRA': 'N/A',   # Substitui NaN em 'PRATELEIRA' por 'N/A'
    'COLUNA': 'N/A',       # Substitui NaN em 'COLUNA' por 'N/A'
    'BANDEIJA': 'N/A',     # Substitui NaN em 'BANDEIJA' por 'N/A'
    'PRECO': 0             # Substitui NaN em 'PRECO' por 0
})
# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdestoque'
)
cursor = conn.cursor()



# Inserir dados no banco de dados


data_dict = df.to_dict(orient='records')


for record in data_dict:
    produto = record['PRODUTO']
    MARCA = record['MARCA']
    MODELO = record['MODELO']
    DESCRICAO = record['DESCRICAO']
    PRATELEIRA = record['PRATELEIRA']
    COLUNA = record['COLUNA']
    BANDEIJA = record['BANDEIJA']
    PRECO = record['PRECO']

    cursor.execute("INSERT INTO estoque (PRODUTO,MARCA,MODELO,DESCRICAO,PRATELEIRA,COLUNA,BANDEIJA,PRECO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (produto,MARCA,MODELO,DESCRICAO,PRATELEIRA,COLUNA,BANDEIJA,PRECO))


