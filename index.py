from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

jan = Tk()
jan.title("System - Acess Panel")
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




def Word():
    Word = WordEntry.get()

    database.cursor.execute(""" 
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (Word))

RemoveButton = ttk.Button(RightFrame, text="Remove", width=30, command=Word)  # Corrigindo o comando para chamar a função Login
RemoveButton.place(x=100, y=200)

def Vocal():
    RemoveButton.place(x=5000)
    
    def RemoveToDataBase(): 
        Word = WordEntry.get()

        if (Word == ""):
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preencha todos os campos.")
            return
        else:
            database.cursor.execute("""
            INSERT INTO Users(Word) VALUES (?, ?, ?, ?)
            """, (Word))  
            database.conn.commit()
            messagebox.showinfo(title="Register Info", message="Palavra registrada com sucesso")



#RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
#RegisterButton.place(x=125, y=260)

jan.mainloop()
