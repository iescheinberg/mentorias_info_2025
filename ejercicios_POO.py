# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def presentarse(self):
#         print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")


# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre, edad)
#         self.carrera = carrera
    
#     def datos_estudiante(self):
#         print(f"Soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}")

# estudiante_2 = Estudiante("Carlos", 26, "Ingenieria")
# estudiante_2.datos_estudiante()









# class Producto:
#     def __init__(self, nombre, precio, stock):
#         self.nombre = nombre
#         self.precio = precio
#         self.stock = stock

#     def mostrar_info(self):
#         print(f"Nombre: {self.nombre} - ${self.precio} - Stock: {self.stock} unidades.")

#     def vender(self):
#         if self.stock > 0:
#             self.stock -= 1
#             print(f"Producto vendido. Quedan {self.stock} unidades.")
#         else:
#             print(f"No hay mas stock disponible.")

# producto_1 = Producto("Iphone 16", 800, 1)
# producto_1.vender()
# producto_1.vender()


# Clase Base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print("El vehiculo esta en marcha!")


# Subclase Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def tocar_bocina(self):
        print("Beep Beep!")

    def tipo_vehiculo(self):
        print(f"Soy un auto")

# Subclase Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def hacer_wheelie(self):
        print("Haciendo wheelie!!")

    def tipo_vehiculo(self):
        print("Soy una moto")

auto_1 = Auto("BMW", "M5")
moto_1 = Moto("Susuki", "100")

vehiculos = [auto_1, moto_1]

for vehiculo in vehiculos:
    vehiculo.tipo_vehiculo()


















