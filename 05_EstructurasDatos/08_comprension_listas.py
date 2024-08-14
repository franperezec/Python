# Comprensión de listas
# La comprensión de listas es una forma concisa de crear listas. La sintaxis es la siguiente:

# [expresión for elemento in iterable]
# La expresión se evalúa una vez por cada elemento en el iterable. El resultado de la evaluación se agrega a la lista resultante. Por ejemplo, para crear una lista con los cuadrados de los números del 1 al 5, se puede hacer lo siguiente:

usuarios = [["Juan", 25], ["María", 30], ["Pedro", 22], ["Luis", 27]]

# Crear una lista con los nombres de los usuarios con for

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])

print(nombres)

# Crear una lista con los nombres de los usuarios con comprensión de listas

# se puede poner cualquier cosa en lugar de usuario
nombres = [usuario[0] for usuario in usuarios]

print(nombres)  # ['Juan', 'María', 'Pedro', 'Luis']

# Crear una lista con los nombres de los usuarios que tienen menos de 25 años Filter

nombres = [usuario[0] for usuario in usuarios if usuario[1] < 25]

print(nombres)  # ['Pedro']

# filtrar y modificar

nombres = [usuario[0] +
           " es menor de 25" for usuario in usuarios if usuario[1] < 25]

print(nombres)  # ['Pedro es menor de 25']


# Usar map y filter
#map
nombres = list(map(lambda usuario: usuario[0]))
print(nombres)  # ['Juan', 'María', 'Pedro', 'Luis']

#filter
nombres = list(filter(lambda usuario: usuario[1] < 25, usuarios))   
print(nombres)  # [['Pedro', 22]]




















