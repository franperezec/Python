# For loop
# Nos puede servir para recorrer una lista, tupla, diccionario, etc.
# usos comunes:
# - Recorrer una lista
# - Recorrer un rango de números
# - Recorrer un diccionario
# - Recorrer una cadena de texto
# - Recorrer una lista de listas
# - Recorrer una matriz
# - Recorrer un archivo
# - Recorrer un objeto iterable
# - Recorrer un objeto iterable con un índice

for numero in range(10):
    print(numero)

# range(10) genera una secuencia de números desde 0 hasta 9
# range(10) es equivalente a range(0, 10, 1)

# podemos formar figuras con for loops
for i in range(5):
    print("*" * (i + 1))


"""For loop con else"""
# podemos usar un else en un for loop, que se ejecutará al finalizar el loop

objetivo = 5
for numero in range(10):
    if numero == objetivo:
        print(f"Se encontró el número {objetivo}")
        break
else:
    print(f"No se encontró el número {objetivo}")


"""Iterables"""
# podemos recorrer una lista
nombres = ["Juan", "María", "Carlos", "Luisa"]
for nombre in nombres:
    print(nombre)


# podemos recorrer un diccionario
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá"
}
for clave, valor in persona.items():
    print(clave, valor)

# podemos recorrer una cadena de texto
mensaje = "Hola mundo"
for letra in mensaje:
    print(letra)

# podemos recorrer una lista de listas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()

# podemos recorrer un archivo
with open(r"C:\PythonCourse\03_ControlFlujo\archivo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea, end='')

# podemos recorrer un objeto iterable


class ListaNumeros:
    def __init__(self):
        self.numeros = [1, 2, 3, 4, 5]

    def __iter__(self):
        return iter(self.numeros)


numeros = ListaNumeros()
for numero in numeros:
    print(numero)

# podemos recorrer un objeto iterable con un índice
for indice, numero in enumerate(numeros):
    print(indice, numero)
# enumerate() nos devuelve una tupla con el índice y el valor del objeto iterable

# podemos recorrer un rango de números
for numero in range(1, 11):
    print(numero)

# podemos recorrer un rango de números con un incremento
for numero in range(0, 11, 2):
    print(numero)

# podemos recorrer un rango de números con un decremento
for numero in range(10, 0, -1):
    print(numero)

# podemos recorrer una tupla
tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    print(numero)

# podemos recorrer un set
conjunto = {1, 2, 3, 4, 5}
for numero in conjunto:
    print(numero)

# podemos recorrer un string
cadena = "Hola mundo"
for letra in cadena:
    print(letra)
