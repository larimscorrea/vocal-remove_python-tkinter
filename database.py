import sqlite3

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()

# Crie a tabela Users se ainda não existir
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Word TEXT NOT NULL
);
""")


print("Conectado com banco de dados!")
