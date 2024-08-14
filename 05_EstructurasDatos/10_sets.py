# conjuntos o sets en Python

# Los conjuntos o sets son una estructura de datos que permite almacenar varios elementos de forma desordenada.

# Los conjuntos son mutables, es decir, se pueden modificar una vez creados.

# Los conjuntos se crean utilizando llaves y separando los elementos con comas.

# Ejemplo de conjunto

conjunto = {1, 2, 3, 4, 5}

conjunto.add(6)
conjunto.remove(1)
print(conjunto)

# Los conjuntos no permiten elementos duplicados, por lo que si intentamos añadir un elemento que ya existe en el conjunto, no se añadirá.

# crear un conjunto con base a una lista

lista = [1, 2, 3, 4, 5, 5, 1, 2, 3, 4]

conjunto2 = set(lista)

print(conjunto2)

# Los conjuntos son útiles para realizar operaciones de conjuntos, como la unión, la intersección, la diferencia y la diferencia simétrica.

# Unión de conjuntos

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

union = conjunto1.union(conjunto2)
print(union)
print(conjunto1 | conjunto2)

# Intersección de conjuntos

interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
print(conjunto1 & conjunto2)

# Diferencia de conjuntos

diferencia = conjunto1.difference(conjunto2)
print(diferencia)
print(conjunto1 - conjunto2)

# Diferencia simétrica de conjuntos

diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)
print(conjunto1 ^ conjunto2)

# no puedo acceder a elementos específicos de un conjunto, ya que no tienen un índice.

# acceder con un for a un conjunto

for elemento in conjunto:
    print(elemento)

# verificar si un elemento está en un conjunto
if 5 in conjunto:
    print("El 5 está en el conjunto")

# Los conjuntos son útiles para eliminar elementos duplicados de una lista.

# eliminar elementos duplicados de una lista

lista = [1, 2, 3, 4, 5, 5, 1, 2, 3, 4]

conjunto = set(lista)

lista_sin_duplicados = list(conjunto)

print(lista_sin_duplicados)
