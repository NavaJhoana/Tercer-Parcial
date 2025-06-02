import tkinter as tk
from tkinter import messagebox

class Triangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0

    def leer_datos(self, base_str, altura_str):
        try:
            self.base = float(base_str)
            self.altura = float(altura_str)
            return True
        except ValueError:
            return False

    def calcular_area(self):
        return (self.base * self.altura) / 2

class App:
    def __init__(self, root):
        self.triangulo = Triangulo()

        root.title("Área de un Triángulo")

        tk.Label(root, text="Base:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_base = tk.Entry(root)
        self.entry_base.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Altura:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_altura = tk.Entry(root)
        self.entry_altura.grid(row=1, column=1, padx=5, pady=5)

        self.btn_calcular = tk.Button(root, text="Calcular área", command=self.calcular)
        self.btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_resultado = tk.Label(root, text="Área: ")
        self.label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

    def calcular(self):
        base = self.entry_base.get()
        altura = self.entry_altura.get()
        if self.triangulo.leer_datos(base, altura):
            area = self.triangulo.calcular_area()
            self.label_resultado.config(text=f"Área: {area:.2f}")
        else:
            messagebox.showerror("Error", "Por favor ingresa números válidos para base y altura.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
