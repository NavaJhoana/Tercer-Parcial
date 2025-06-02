class Triangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0

    # Función para leer los datos
    def leer_datos(self):
        self.base = float(input("Ingresa la base del triángulo: "))
        self.altura = float(input("Ingresa la altura del triángulo: "))

    # Función para calcular el área
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Código principal
t = Triangulo()        
t.leer_datos()           
print("El área es:", t.calcular_area())  
