# Operaciones con listas en Python: Ejemplo con lista de mascotas

def imprimir_lista(lista, mensaje="Lista actual:"):
    print(f"\n{mensaje}")
    print(lista)


# Creación de la lista inicial
mascotas = ['perro', 'gato', 'loro', 'pez', 'hamster']
imprimir_lista(mascotas, "Lista inicial de mascotas:")
# Salida: ['perro', 'gato', 'loro', 'pez', 'hamster']

# 1. Agregar un elemento en una posición específica
# insert(índice, elemento) - Inserta 'elemento' en la posición 'índice'
mascotas.insert(1, 'conejo')
imprimir_lista(mascotas, "Después de agregar 'conejo' en la segunda posición:")
# Salida: ['perro', 'conejo', 'gato', 'loro', 'pez', 'hamster']

# 2. Agregar un elemento al final de la lista
# append(elemento) - Añade 'elemento' al final de la lista
mascotas.append('puerquito')
imprimir_lista(mascotas, "Después de agregar 'puerquito' al final:")
# Salida: ['perro', 'conejo', 'gato', 'loro', 'pez', 'hamster', 'puerquito']

# 3. Eliminar un elemento específico
# remove(elemento) - Elimina la primera ocurrencia de 'elemento'
mascotas.remove('pez')
imprimir_lista(mascotas, "Después de eliminar 'pez':")
# Salida: ['perro', 'conejo', 'gato', 'loro', 'hamster', 'puerquito']

# 4. Eliminar el primer elemento
# pop(índice) - Elimina y retorna el elemento en la posición 'índice'
primer_elemento = mascotas.pop(0)
imprimir_lista(
    mascotas, f"Después de eliminar el primer elemento ('{primer_elemento}'):")
# Salida: ['conejo', 'gato', 'loro', 'hamster', 'puerquito']

# 5. Eliminar el último elemento
# pop() sin argumentos elimina y retorna el último elemento
ultimo_elemento = mascotas.pop()
imprimir_lista(
    mascotas, f"Después de eliminar el último elemento ('{ultimo_elemento}'):")
# Salida: ['conejo', 'gato', 'loro', 'hamster']

# 6. Eliminar un elemento por índice usando 'del'
# del lista[índice] - Elimina el elemento en la posición 'índice'
del mascotas[0]
imprimir_lista(mascotas, "Después de eliminar el primer elemento con 'del':")
# Salida: ['gato', 'loro', 'hamster']

# 7. Eliminar todos los elementos
# clear() - Elimina todos los elementos de la lista
mascotas.clear()
imprimir_lista(mascotas, "Después de eliminar todos los elementos:")
# Salida: []

# 8. Agregar múltiples elementos
# extend(iterable) - Añade todos los elementos del iterable al final de la lista
mascotas.extend(['perro', 'gato', 'loro', 'pez', 'hamster'])
imprimir_lista(mascotas, "Después de agregar múltiples elementos:")
# Salida: ['perro', 'gato', 'loro', 'pez', 'hamster']

print("\n--- Operaciones adicionales ---")

# 9. Modificar un elemento
# Podemos modificar un elemento accediendo directamente a su índice
mascotas[0] = 'perrito'
imprimir_lista(mascotas, "Después de modificar el primer elemento:")
# Salida: ['perrito', 'gato', 'loro', 'pez', 'hamster']

# 10. Obtener la longitud de la lista
# len(lista) - Retorna el número de elementos en la lista
print(f"\nNúmero de mascotas: {len(mascotas)}")
# Salida: Número de mascotas: 5

# 11. Buscar un elemento en la lista
mascota_buscar = 'gato'
if mascota_buscar in mascotas:
    # index(elemento) - Retorna el índice de la primera ocurrencia de 'elemento'
    print(f"\n'{mascota_buscar}' está en la lista en la posición {
          mascotas.index(mascota_buscar)}")
else:
    print(f"\n'{mascota_buscar}' no está en la lista")
# Salida: 'gato' está en la lista en la posición 1

# 12. Ordenar la lista
# sort() - Ordena la lista in-place (modifica la lista original)
mascotas.sort()
imprimir_lista(mascotas, "Lista ordenada alfabéticamente:")
# Salida: ['gato', 'hamster', 'loro', 'perrito', 'pez']

# 13. Invertir la lista
# reverse() - Invierte el orden de los elementos in-place
mascotas.reverse()
imprimir_lista(mascotas, "Lista invertida:")
# Salida: ['pez', 'perrito', 'loro', 'hamster', 'gato']

# Nota: También puedes usar sorted(lista) para obtener una nueva lista ordenada
# y lista[::-1] para obtener una nueva lista invertida sin modificar la original.
