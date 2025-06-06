# 1- Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla.
# Declaro la variable en primer lugar y solicito un nombre
# nombre = input("Ingrese un nombre de usuario: ")
# print("Nombre de usuario es:", nombre)


# 2. Crea un programa que calcule la suma de dos números enteros y lo imprima en pantalla y luego calcular su doble
# Primero declara variables
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# # Puedo o no crear una variable suma, si no lo hago, directamente hago en el print la suma e imprimo.
# suma = num1 + num2
# print(f"La suma de los numeros es {suma} y su doble es {suma*2}")


# 3. Escribir un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad (18 años o más) o no.
# edad = int(input("Ingrese su edad: "))
# if edad > 17: 
#     print("Es mayor de edad")
# else:
#     print("No es mayor de edad")


# 4. Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC).
# IMC = peso / estatura**2

# peso = float(input("Ingrese su peso en kilogramos: "))
# estatura = float(input("Ingrese su altura en metros: "))
# imc = peso / estatura ** 2

# print(f"Su IMC es de {imc:.2f}")


# 7. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.
# numero = int(input("Ingrese un numero entero: "))

# if (numero % 2 == 0) and (numero % 3 == 0):
#     print(f"El numero {numero} es multiplo de 2 y de 3 a la vez")
# else:
#     print(f"El numero {numero} NO es multiplo de 2 y de 3 a la vez")

# 8. Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.

# caracter = input("Ingrese un caracter: ")

# if caracter.islower():
#     print("Minuscula")
# elif caracter.isupper():
#     print("Mayuscula")
# elif caracter.isdigit():
#     print("Numero")
# else:
#     print("Caracter especial")

# 9. Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a".
# cadena = input("Ingrese una cadena de caracteres: ")
# Primer forma
# if "a" in cadena.lower():
#     print("La cadena contiene 'a'.")
# else:
#     print("La cadena NO contiene 'a'.")


# Segunda forma
# contiene_a = False

# for caracter in cadena:
#     if caracter.lower() == 'a':
#         contiene_a = True
#         break
# if contiene_a:
#     print("contiene a")
# else:
#     print("no contiene a")

# 10. Crear un programa que pida usuario y contraseña, en caso de ser incorrectas, volver a pedir.
""" USUARIO_VALIDO = "Info"
CONTRASENA_VALIDA = "1234"


while True:
    usuario = input("Usuario >> ")
    contrasena = input("Contraseña >> ")

    if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
        print(f"Acceso concedido Bienvenido {usuario}!")
        break
    else:
        print("Usuario / contraseña incorrectos. Intentalo de nuevo.") """

# Modificar este ejercicio ahora con numero de intentos validos.


# Hoja de ejercicios - Estructuras de datos
# 5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto.
""" numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numeros)
 """

# 6- Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número de elementos en el conjunto.
""" numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
impares = set()

for numero in numeros:
    if numero % 2 != 0:
        impares.add(numero)
print(impares) """

# 1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y mostrar el diccionario completo.
""" frutas = {
    "Manzana" : 3500.5,
    "Naranja" : 2500.68,
    "Banana" : 2800.34
}
for fruta, precio in frutas.items():
    print(f"Fruta: {fruta}, Precio ${precio}") """


# 9-Crear una lista con los nombres de tres países y ordenar la lista en orden alfabético. Mostrar la lista resultante.
numeros = [2, 6, 1, 7, 3, 9]
ordenados = sorted(numeros)
print(ordenados)
print(numeros)
