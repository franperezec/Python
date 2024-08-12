x = input("")

# int(x) convierte x a un entero
# float(x) convierte x a un número decimal
# str(x) convierte x a una cadena de texto
# bool(x) convierte x a un valor booleano
# list(x) convierte x a una lista
# tuple(x) convierte x a una tupla
# set(x) convierte x a un conjunto
# dict(x) convierte x a un diccionario
# chr(x) convierte x a un carácter
# ord(x) convierte x a un número entero
# hex(x) convierte x a una cadena hexadecimal
# oct(x) convierte x a una cadena octal
# bin(x) convierte x a una cadena binaria
# complex(x) convierte x a un número complejo
# bytes(x) convierte x a una secuencia de bytes
# bytearray(x) convierte x a un arreglo de bytes
# memoryview(x) convierte x a una vista de memoria
# type(x) devuelve el tipo de x
# id(x) devuelve el identificador de x


# Ejemplo de conversión de tipos
x = "10"
print(type(x))  # <class 'str'>
x = int(x)
print(type(x))  # <class 'int'>
print(x)  # 10

# Ejemplo de conversión de tipos
x = 10
print(type(x))  # <class 'int'>
x = str(x)
print(type(x))  # <class 'str'>
print(x)  # "10"

print(bool(""))  # False
print(bool("Hola"))  # True
print(bool(0))  # False
print(bool(1))  # True
print(bool([]))  # False
print(bool(None))  # False
