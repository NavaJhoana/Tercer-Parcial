class Dispositivo:
    def __init__(self, marca,modelo,procesador,pantalla):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.pantalla=pantalla

    def encender(self):
        print(f"{self.marca} {self.modelo} se está encendiendo.")

    def apagar(self):
        print(f"{self.marca} {self.modelo} se está apagando.")
        
    def Informacion(self): 
        print(f"Tu dispositivo es un: {self.modelo}, de la marca: {self.marca} con una pantalla {self.pantalla} y un procesador {self.procesador}")   

class Telefono(Dispositivo):
    def llamar(self, numero):
        print(f"Llamando al número {numero} desde {self.marca} {self.modelo}.")

class Computadora(Dispositivo):
    def ejecutar_programa(self, programa):
        print(f"Ejecutando el programa '{programa}' en {self.marca} {self.modelo}.")

class Tableta(Dispositivo):
    def dibujar(self):
        print(f"Dibujando en la pantalla de la tableta {self.marca} {self.modelo}.")

def main():
    while True:
     print("/n")   
     print("Elige el tipo de dispositivo:")
     print("1. Teléfono")
     print("2. Computadora")
     print("3. Tableta")
     print("4.Salir del programa")
    
     opcion = input("Ingresa una opción (1-4): ")
    
     if opcion == "1":
         marca = input("Ingresa la marca del telefono: ")
         modelo = input("Ingresa el modelo del telefono: ")
         procesador=input("Ingresa el procesador del telefono: ")
         pantalla=input("Ingresa la el tipo de pantalla del telefono: ")
         telefono = Telefono(marca,modelo,procesador,pantalla)
         telefono.encender()
         numero = input("Ingresa el número al que quieres llamar: ")
         telefono.llamar(numero)
         opc1=input("Deseas acceder a la informacion de tu dispositivo? (si/no)")
         if opc1=="si":
             telefono.Informacion()
         elif opc1=="no":
              telefono.apagar()
         else:
             print("Opcion no valida")        
         
     elif opcion == "2":
         marca = input("Ingresa la marca de la computadora: ")
         modelo = input("Ingresa el modelo de la computadora: ")
         procesador=input("Ingresa el procesador de la computadora: ")
         pantalla=input("Ingresa la el tipo de pantalla de la computadora: ")
         computadora = Computadora(marca,modelo,procesador,pantalla)
         computadora.encender()
         programa = input("Ingresa el nombre del programa que quieres ejecutar: ")
         computadora.ejecutar_programa(programa)
         opc2=input("Deseas acceder a la informacion de tu dispositivo? (si/no)")
         if opc2=="si":
             computadora.Informacion()
         elif opc2=="no":
              computadora.apagar()
         else:
             print("Opcion no valida") 

    
     elif opcion == "3":
         marca = input("Ingresa la marca de la tableta: ")
         modelo = input("Ingresa el modelo de la tableta: ")
         procesador=input("Ingresa el procesador de la tableta: ")
         pantalla=input("Ingresa la el tipo de pantalla de la tableta: ")
         tableta = Tableta(marca,modelo,procesador,pantalla)
         tableta.encender()
         tableta.dibujar()
         opc3=input("Deseas acceder a la informacion de tu dispositivo? (si/no)")
         if opc3=="si":
             tableta.Informacion()
         elif opc3=="no":
             tableta.apagar()
         else:
             print("Opcion no valida") 
     
     elif opcion=="4":
         print("Saliendo del programa")
         break    
    
     else:
         print("Opción no válida.")

if __name__ == "__main__":
    main()