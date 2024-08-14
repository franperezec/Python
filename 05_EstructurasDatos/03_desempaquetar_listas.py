
# Acceso a los elementos de una lista
mi_lista = [1, 2, 3]

primero = mi_lista[0]
segundo = mi_lista[1]
tercero = mi_lista[2]

print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])

# Desempaquetar listas
primero, segundo, tercero = mi_lista  # Desempaquetar listas

# Desempaquetar listas para obtener el primer elemento y el resto
primero, *resto = mi_lista

print(primero, resto)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *resto = numeros  # Desempaquetar listas
print(primero, segundo, resto)  # 1 2 [3, 4, 5, 6, 7, 8, 9]

primero, *resto, ultimo = numeros  # Desempaquetar listas
print(primero, resto, ultimo)  # 1 [2, 3, 4, 5, 6, 7, 8] 9
