# diccionarios

# Los diccionarios son una estructura de datos que permite almacenar pares clave-valor. Cada clave es única y está asociada a un valor. Los diccionarios son mutables, lo que significa que se pueden modificar después de haber sido creados.

# Los diccionarios se crean utilizando llaves y separando los pares clave-valor con comas. Cada par clave-valor se separa con dos puntos (:).

# Ejemplo de diccionario, así funcionan las bases de datos

diccionario = {'nombre': 'Juan', 'edad': 25,
               'cursos': ['Python', 'Django', 'JavaScript']}

print(diccionario)

# Para acceder a un valor de un diccionario, se utiliza la clave correspondiente entre corchetes.

print(diccionario['nombre'])  # Juan

# Si intentamos acceder a una clave que no existe en el diccionario, se generará un error.

# print(diccionario['apellido']) # KeyError: 'apellido'

if 'apellido' in diccionario:
    print(diccionario['apellido'])

# Para evitar errores al intentar acceder a una clave que no existe, se puede utilizar el método get. Este método recibe como argumento la clave que se desea obtener y un valor por defecto que se retornará en caso de que la clave no exista.

print(diccionario.get('apellido', 'Pérez'))  # Pérez

# Para añadir un nuevo par clave-valor a un diccionario, se utiliza la siguiente sintaxis:

diccionario['apellido'] = 'Pérez'

# {'nombre': 'Juan', 'edad': 25, 'cursos': ['Python', 'Django', 'JavaScript'], 'apellido': 'Pérez'}
print(diccionario)

# eliminar un par clave-valor de un diccionario, se utiliza la instrucción del seguida de la clave que se desea eliminar.

# {'nombre': 'Juan', 'edad': 25, 'cursos': ['Python', 'Django', 'JavaScript']}
del diccionario['apellido']

# Para obtener todas las claves de un diccionario, se utiliza el método keys.

print(diccionario.keys())  # dict_keys(['nombre', 'edad', 'cursos'])

# Para obtener todos los valores de un diccionario, se utiliza el método values.

# dict_values(['Juan', 25, ['Python', 'Django', 'JavaScript']])
print(diccionario.values())

# Para obtener todos los pares clave-valor de un diccionario, se utiliza el método items.

# dict_items([('nombre', 'Juan'), ('edad', 25), ('cursos', ['Python', 'Django', 'JavaScript'])])
print(diccionario.items())

# Para recorrer un diccionario, se puede utilizar un ciclo for. En cada iteración, se obtiene la clave y el valor correspondiente.

for clave, valor in diccionario.items():
    print(clave, valor)

# nombre Juan
# edad 25
# cursos ['Python', 'Django', 'JavaScript']

# Los diccionarios también pueden contener diccionarios como valores.

diccionario = {
    'persona': {
        'nombre': 'Juan',
        'edad': 25
    }
}

print(diccionario)  # {'persona': {'nombre': 'Juan', 'edad': 25}}

# Para acceder a un valor anidado, se utilizan corchetes adicionales.

print(diccionario['persona']['nombre'])  # Juan

# Para añadir un nuevo par clave-valor a un diccionario anidado, se utilizan corchetes adicionales.

diccionario['persona']['apellido'] = 'Pérez'

# {'persona': {'nombre': 'Juan', 'edad': 25, 'apellido': 'Pérez'}}
print(diccionario)

# Para recorrer un diccionario anidado, se utilizan ciclos for anidados.

diccionario = {
    'persona': {
        'nombre': 'Juan',
        'edad': 25
    }
}

for clave, valor in diccionario.items():
    print(clave)
    for clave2, valor2 in valor.items():
        print(clave2, valor2)

# persona
# nombre Juan
# edad 25

# Los diccionarios también pueden contener listas como valores.

diccionario = {
    'persona': ['Juan', 25]
}

print(diccionario)  # {'persona': ['Juan', 25]}
print(diccionario['persona'][0])  # Juan

# Para añadir un nuevo valor a una lista que se encuentra en un diccionario, se utilizan corchetes adicionales.

diccionario['persona'].append('Pérez')

print(diccionario)  # {'persona': ['Juan', 25, 'Pérez']}

# Para recorrer un diccionario que contiene listas como valores, se utilizan ciclos for anidados.

diccionario = {
    'persona': ['Juan', 25]
}

for clave, valor in diccionario.items():
    print(clave)
    for elemento in valor:
        print(elemento)

# persona
# Juan
# 25

# crear un diccionario con id y nombre de personas

personas = [
    {"id": 1, "nombre": 'Juan'},
    {"id": 2, "nombre": 'María'},
    {"id": 3, "nombre": 'Pedro'}
]

for persona in personas:
    print(persona["nombre"])
