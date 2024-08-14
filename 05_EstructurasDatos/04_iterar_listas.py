# Iterar sobre una lista

mi_lista = [1, 2, 3, 4, 5]
for elemento in mi_lista:
    print(elemento)


# Acceso a elementos de listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])
print(matriz[1][2])


mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']
for mascota in mascotas:
    print(mascota)  # perro, gato, loro, pez, hamster

mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']
for mascota in enumerate(mascotas):
    # (0, 'perro'), (1, 'gato'), (2, 'loro'), (3, 'pez'), (4, 'hamster') es una tupla que es un par ordenado
    print(mascota)

mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']
for mascota in enumerate(mascotas):
    print(mascota[0])  # 0, 1, 2, 3, 4

mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']
for mascota in enumerate(mascotas):
    print(mascota[1])  # perro, gato, loro, pez, hamster

mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']
primero, segundo = [1, 2]   # primero = 1, segundo = 2
for indice, mascota in enumerate(mascotas):
    # 0 perro, 1 gato, 2 loro, 3 pez, 4 hamster accediendo a los elementos de la tupla
    print(indice, mascota)
