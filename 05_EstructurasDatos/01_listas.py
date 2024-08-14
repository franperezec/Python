# Listas en Python

# Las listas son una estructura de datos que permite almacenar varios elementos
# en una sola variable. Los elementos pueden ser de cualquier tipo y pueden
# ser accedidos mediante un índice.

# Creación de una lista
# Lista con 5 elementos sus partes son: [0, 1, 2, 3, 4]
numeros = [1, 2, 3, 4, 5]
print(numeros)

letras = ['a', 'b', 'c', 'd']
palabras = ['hola', 'mundo', 'python']

alfanumerico = numeros + letras

print(letras)
print(palabras)
print(alfanumerico)

booleanos = [True, False, True, False]
print(booleanos)

# Listas vacías
lista_vacia = []
print(lista_vacia)

# Listas con elementos de diferentes tipos
mi_lista = [1, "hola", 3.14, True]
print(mi_lista)

# ceros

ceros = [0] * 5  # [0, 0, 0, 0, 0]

# Listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

rango = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rangos = list(range(5, 10))  # [5, 6, 7, 8, 9]

char = list("hola")  # ['h', 'o', 'l', 'a']
