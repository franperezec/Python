# buscar elemento en una lista

mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']

# metodo 1
print(mascotas.index('loro'))  # 2
print(mascotas.index('periquito'))  # ValueError: 'periquito' is not in list

# saber si un elemento esta en la lista
if 'periquito' in mascotas:
    print(mascotas.index('periquito'))
else:
    print('periquito no esta en la lista')

# saber cuántas veces se repite un elemento en la lista
print(mascotas.count('loro'))  # 1
