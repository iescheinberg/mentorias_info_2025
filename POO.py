
# POO

# Pelota es esferica
# colo negro y blanco
# peso
# textura
# rueda
# Un objeto es una instancia de clase
""" class Pelota:
    def __init__(self, color, marca, tamano, deporte):
        self.color = color
        self.marca = marca
        self.tamano = tamano
        self.deporte = deporte
    
    def rodar(self):
        print(f"La pelota de {self.deporte} esta rodando!!")

mi_pelota1 = Pelota("blanca", "Nike", 5, "Futbol")
mi_pelota2 = Pelota("roja", "Adidas", 3, "Futsal")

print(f"Mi pelota es {mi_pelota1.marca}, de color {mi_pelota1.color}")
mi_pelota1.rodar() """

# -----------------------------------------------------------------------------------------------------
# Calculadora con POO

class Calculadora:
    # Atributos -> como variables
    def __init__(self):
        pass
    # Metodos -> como funciones
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error. División por 0."

mi_calculadora = Calculadora()
print(f"Suma: {mi_calculadora.sumar(7, 5)}")
print(f"Suma: {mi_calculadora.restar(7, 5)}")
print(f"Suma: {mi_calculadora.multiplicar(3, 5)}")
print(f"Suma: {mi_calculadora.dividir(12, 3)}")