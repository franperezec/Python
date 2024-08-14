# Manipulación de listas

# Creación de una lista
# Lista con 4 elementos sus partes son: [0, 1, 2, 3]
mascotas = ['perro', 'gato', 'pez', 'canario']
print(mascotas[0])

mascotas[0] = 'loro'
print(mascotas)  # ['loro', 'gato', 'pez', 'canario']

# ['gato', 'pez'] imprime los elementos desde el índice 1 hasta el índice 3
print(mascotas[1:3])
# ['loro', 'gato'] imprime los elementos desde el inicio hasta el índice 2
print(mascotas[:2])
# ['pez', 'canario'] imprime los elementos desde el índice 2 hasta el final
print(mascotas[2:])

print(mascotas[-1])  # canario imprime el último elemento de la lista
print(mascotas[-2])  # pez imprime el penúltimo elemento de la lista
# ['gato', 'pez', 'canario'] imprime los últimos 3 elementos de la lista
print(mascotas[-3:])
# ['loro', 'gato'] imprime los elementos desde el inicio hasta el penúltimo
print(mascotas[:-2])

# ['canario', 'pez', 'gato', 'loro'] imprime la lista en orden inverso
print(mascotas[::-1])

# ['loro', 'pez'] imprime los elementos de la lista saltando de 2 en 2
print(mascotas[::2])

# ['gato'] imprime los elementos desde el índice 1 hasta el índice 3 saltando de 2 en 2
print(mascotas[1:3:2])

# ['gato', 'canario'] imprime los elementos desde el índice 1 hasta el final saltando de 2 en 2
print(mascotas[1::2])

# ['loro', 'gato', 'pez', 'canario', 'loro', 'gato', 'pez', 'canario'] imprime la lista duplicada
print(mascotas * 2)

# ['loro', 'gato', 'pez', 'canario', 'hamster', 'conejo'] imprime la lista concatenada con ['hamster', 'conejo']
print(mascotas + ['hamster', 'conejo'])

# True imprime True si el elemento 'gato' está en la lista
print('gato' in mascotas)

print(mascotas.index('pez'))  # 2 imprime el índice del elemento 'pez'


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros = list(range(21))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] imprime los números pares de la lista
print(numeros[::2])
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] imprime los números impares de la lista
print(numeros[1::2])

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] crea una lista con los números impares de 1 a 20
numeros2 = list(range(1, 21))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] imprime los números impares de la lista
print(numeros2[::2])

# [0, 1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0, 13, 0, 15, 0, 17, 0, 19, 0] asigna el valor 0 a los números pares
numeros[::2] = [0] * 11
