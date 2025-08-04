import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class PasswordApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Cofre de passwords")
        self.root.geometry("400x300")
        self.pdf_files=[]

        tk.Label(root, text="Usuario: ").pack()
        entrada_usuario = tk.Entry(root)
        entrada_usuario.pack()

        tk.Label(root, text="Contrasena: ").pack()
        entrada_contrasena = tk.Entry(root)
        entrada_contrasena.pack()

        ttk.Button(root, text="Guardar cuenta", command=self.save_account).pack(pady=10)
        
    def save_account(self):
        print("ok")
  


if __name__ == "__main__":
    root =tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
