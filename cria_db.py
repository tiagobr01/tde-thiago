import sqlite3

conn = sqlite3.connect(".\\database\\portaldb")
cursor = conn.cursor()

sql = """CREATE TABLE trabalhos (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(100) NOT NULL, descricao VARCHAR(100) NOT NULL,resumo VARCHAR(100) NOT NULL,data_entrega DATE,autores VARCHAR(100) NOT NULL,orientador VARCHAR(100) NOT NULL,palavras VARCHAR(100) NOT NULL);"""
cursor.execute(sql)
print("Banco de dados criado com sucesso")
cursor.close()
conn.close()