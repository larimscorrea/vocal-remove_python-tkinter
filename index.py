from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

database.create_table()

jan = Tk()
jan.title("System - Access Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

LeftFrame = Frame(jan, width=200, height=300, bg="#FFD700", relief="raised")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="#FFD700", relief="raised")
RightFrame.pack(side=RIGHT)

WordLabel = Label(RightFrame, text="Word: ", font=("Century Gothic", 20), bg="#FFD700", fg="white")
WordLabel.place(x=5, y=100)

WordEntry = ttk.Entry(RightFrame, width=30)
WordEntry.place(x=150, y=110)

def RemoveVowels():
    word = WordEntry.get()
    if not word:
        messagebox.showerror(title="Error", message="Please enter a word.")
        return

    # Remover vogais
    vowels = "aeiouAEIOU"
    word_without_vowels = "".join([char for char in word if char not in vowels])

    # Armazenar no banco de dados
    database.cursor.execute("INSERT INTO Words(Word) VALUES (?)", (word_without_vowels,))
    database.conn.commit()

    messagebox.showinfo(title="Success", message=f"Word '{word}' without vowels has been stored successfully.")

RemoveButton = ttk.Button(RightFrame, text="Remove", width=30, command=RemoveVowels)
RemoveButton.place(x=100, y=200)

jan.mainloop()
