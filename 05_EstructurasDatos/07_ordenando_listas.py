# ordenando_listas.py

# Ordenando listas de un conjunto de números aleatorios
import random

# Creación de una lista de 10 números aleatorios
numeros = [random.randint(0, 100) for _ in range(10)]

# Imprimir la lista de números
print("Lista de números:")
print(numeros)

# Longitud de una lista
print(len(numeros))

# Ordenar la lista de números
numeros.sort()  # Ordena la lista de menor a  para ver las opciones se borra parentesis y se abre parentesis o se pone punto o se presiona ctrl + espacio
print("Lista de números ordenada:")
print(numeros)

# Ordenar la lista de números de mayor a menor
numeros.sort(reverse=True)
print("Lista de números ordenada de mayor a menor:")
print(numeros)

# Ordena la lista de menor a mayor sin modificar la lista original
numeros2 = sorted(numeros)
# Ordena la lista de mayor a menor sin modificar la lista original
numeros3 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)
print(numeros3)


usuarios = [["Juan", 25], ["María", 30], ["Pedro", 22], ["Luis", 27]]


def ordenar_por_edad(usuario):
    return usuario[1]


usuarios.sort(key=ordenar_por_edad)  # Ordena la lista de usuarios por la edad

# Ordena la lista de usuarios por la edad de mayor a menor
usuarios.sort(key=ordenar_por_edad, reverse=True)

# usando una función lambda si no se va a reutilizar la función

# Ordena la lista de usuarios por la edad
usuarios.sort(key=lambda usuario: usuario[1])

# Ordena la lista de usuarios por la edad de mayor a menor
usuarios.sort(key=lambda usuario: usuario[1], reverse=True)
