# tuplas

# Las tuplas son una estructura de datos que permite almacenar varios elementos de forma ordenada.
# se usan cuando se necesita almacenar varios elementos de forma ordenada y no se van a modificar.

# Las tuplas son inmutables, es decir, no se pueden modificar una vez creadas.

# Las tuplas se crean utilizando paréntesis y separando los elementos con comas.

# Ejemplo de tupla

numeros = (1, 2, 3, 4, 5)
print(numeros)  # (1, 2, 3, 4, 5)

# acceder a un elemento de una tupla, no se puede modificar usar append, insert, remove, pop, etc.

menos_numeros = numeros[1:4]

# desempaquetar una tupla

primero, segundo, *resto = numeros
print(primero)  # 1

# desempaquetar con un for

for numero in numeros:
    print(numero)

# transformar una lista en una tupla

numeros = [1, 2, 3, 4, 5]
tupla = tuple(numeros)

print(tupla)  # (1, 2, 3, 4, 5)

# transformar una tupla en una lista

numeros = (1, 2, 3, 4, 5)
lista = list(numeros)

print(lista)  # [1, 2, 3, 4, 5]
