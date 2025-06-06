class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")



class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    
    def datos_estudiante(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}")

estudiante_1 = Estudiante("José", 25, "Arquitectura")
estudiante_1.datos_estudiante()





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
















