import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
import os


class PasswordApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Cofre de passwords")
        self.root.geometry("400x300")
        self.pdf_files=[]

        #obtener la ruta del directorio donde esta este script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        #construir la ruta al archivo CSV
        csv_path=os.path.join(script_dir,"data","passwords.csv")

        self.df=pd.read_csv(csv_path)
         

        tk.Label(root, text="Usuario: ").pack()
        self.entrada_usuario = tk.Entry(root)
        self.entrada_usuario.pack()

        tk.Label(root, text="Contrasena: ").pack()
        self.entrada_contrasena = tk.Entry(root)
        self.entrada_contrasena.pack()

        ttk.Button(root, text="Guardar cuenta", command=self.save_account).pack(pady=10)
        
    def save_account(self):
        self.df.loc[len(self.df)] = [self.entrada_usuario.get(), self.entrada_contrasena.get()]
        print(str(self.df) + "\n")
        print("ok")
  


if __name__ == "__main__":
    root =tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
