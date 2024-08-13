# Funciones en Python

def hola():
    print("Hola Mundo")
    print("Hoy es un buen día")


hola()  # Llamamos a la función hola dos espacios en blanco luego de la definición de la función

# Función con parámetros


def hola2(nombre):  # nombre es un parámetro de la función hola2
    print(f"Hola {nombre}")
    print("Hoy es un buen día")


hola2("Francisco")  # Llamamos a la función hola2 con el argumento "Francisco"


def hola3(nombre, apellido):  # nombre y apellido son parámetros de la función hola3
    print(f"Hola {nombre} {apellido}")
    print("Hoy es un buen día")


# Llamamos a la función hola3 con los argumentos "Francisco" y "Pérez"
hola3("Francisco", "Pérez")

# Función con parámetros por defecto

# nombre es un parámetro de la función hola4 con un valor por defecto "Mundo"
# los parámetros con valores por defecto deben ir después de los parámetros sin valores por defecto


def hola4(apellido="", nombre="Sr."):
    print(f"Hola {nombre} {apellido}")
    print("Hoy es un buen día")


hola4()  # Llamamos a la función hola4 sin argumentos
hola4("Francisco")  # Llamamos a la función hola4 con el argumento "Francisco"
# Llamamos a la función hola4 con los argumentos "Francisco" y "Pérez"
hola4("Pérez", "Francisco")

# Argumentos nombrados
# Llamamos a la función hola4 con los argumentos "Francisco" y "Pérez"
hola4(nombre="Francisco", apellido="Pérez")
