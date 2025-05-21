
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error. División por 0."


# Principal
print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Input de opciones 
opcion = input("Elige una de las opciones: ")

# Declaro las variables y pido valor.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Condicional para ejecutar funciones
if opcion == "1":
    print("Resultado: ", sumar(num1, num2))
elif opcion == "2":
    print("Resultado: ", restar(num1, num2))
elif opcion == "3":
    print("Resultado: ", multiplicar(num1, num2))
elif opcion == "4":
    print("Resultado: ", dividir(num1, num2))
else:
    print("Opción inválida.")









