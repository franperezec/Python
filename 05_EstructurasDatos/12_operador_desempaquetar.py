# operador de desempaquetado

# El operador de desempaquetado se utiliza para desempaquetar los elementos de una lista o un diccionario.

# Desempaquetar una lista

# Para desempaquetar los elementos de una lista, se utiliza el operador de desempaquetado *.

lista = [1, 2, 3, 4, 5]

print(*lista)  # 1 2 3 4 5

# Desempaquetar una tupla

# Para desempaquetar los elementos de una tupla, se utiliza el operador de desempaquetado *.

tupla = (1, 2, 3, 4, 5)

print(*tupla)  # 1 2 3 4 5

# crear una lista compuesta por los elementos de dos listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_combinada = [*lista1, *lista2]

# podemos agregar elementos adicionales a la lista combinada
lista_combinada = [*lista1, *lista2, 10]
lista_combinada.append(7)

# Desempaquetar un diccionario

# dos diccionarios

diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}

# combinar los dos diccionarios en un nuevo diccionario

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
diccionario_combinado = {**diccionario1, **diccionario2}

# los valores se asignan de izquierda a derecha, si hay claves repetidas, se toma el valor de la derecha

diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}

diccionario_combinado = {**diccionario1, **
                         diccionario2}  # {'a': 1, 'b': 3, 'c': 4}

# Desempaquetar un diccionario con el operador de desempaquetado **

# Para desempaquetar los elementos de un diccionario, se utiliza el operador de desempaquetado **.

diccionario = {'a': 1, 'b': 2, 'c': 3}


def funcion(a, b, c):
    print(a, b, c)


funcion(**diccionario)  # 1 2 3
