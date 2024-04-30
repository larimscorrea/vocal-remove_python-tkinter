import sqlite3

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()

# Crie a tabela Users se ainda não existir

def create_table():
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Words (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Word TEXT NOT NULL
    );
""")


print("Conectado com banco de dados!")


if __name__ == "__main__":
    create_table()
    print("Table created successfully!")
