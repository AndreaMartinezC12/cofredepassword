import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
import os
import bcrypt

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
         
        tk.Label(root, text="Aplicacion: ").pack()
        self.entrada_aplicacion = tk.Entry(root)
        self.entrada_aplicacion.pack()

        tk.Label(root, text="Usuario: ").pack()
        self.entrada_usuario = tk.Entry(root)
        self.entrada_usuario.pack()

        tk.Label(root, text="Contrasena: ").pack()
        self.entrada_contrasena = tk.Entry(root)
        self.entrada_contrasena.pack()

        ttk.Button(root, text="Guardar cuenta", command=self.save_account).pack(pady=10)

        tk.Label(root, text="Busqueda: ").pack()
        self.entrada_busqueda = tk.Entry(root)
        self.entrada_busqueda.pack()

        tk.Label(root, text="Buscar por: ").pack()
        # Create a StringVar to hold the combobox's value
        selected_option = tk.StringVar()

        # Create the Combobox
        self.my_combobox = ttk.Combobox(root, textvariable=selected_option,
                           values=("Aplicacion", "Usuario"))
        self.my_combobox.set("Select") # Set initial display text

        # Bind the <<ComboboxSelected>> event to a function
        self.my_combobox.bind("<<ComboboxSelected>>", self.set_tipobusqueda)

        self.my_combobox.pack(pady=10)

        ttk.Button(root, text="Buscar", command=self.search_account).pack(pady=10)

        self.lblresultado = tk.Label(root, text="", justify="left",)
        self.lblresultado.pack()
        
    def save_account(self):
        password = self.entrada_contrasena.get().encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        self.df.loc[len(self.df)] = [self.entrada_aplicacion.get(), self.entrada_usuario.get(), hashed]
        print(str(self.df) + "\n")

    def set_tipobusqueda(self, event):
        selected_value = self.my_combobox.get()
        print(f"Selected: {selected_value}")

    def search_account(self):
        tipo_busqueda = self.my_combobox.get()
        if tipo_busqueda == "Aplicacion":
            result = self.df[self.df['Aplicacion'].str.contains(self.entrada_busqueda.get(), na=False)]
        elif tipo_busqueda == "Usuario":
            result = self.df[self.df['User'].str.contains(self.entrada_busqueda.get(), na=False)]
        else:
            messagebox.showinfo("Error en busqueda", "Selecciona 'aplicacion' o 'usuario' como tipo de busqueda")

        if result.empty:
            messagebox.showinfo("Sin resultados", "No se encontraron resultados")
        else:
            self.lblresultado.configure(text = result)
            
  

if __name__ == "__main__":
    root =tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
