animal = "gato tricolor"
print(animal.upper())  # GATO TRICOLOR convierte la cadena a mayúsculas
print(animal.lower())  # gato tricolor convierte la cadena a minúsculas
# Gato tricolor convierte la primera letra de la cadena a mayúsculas
print(animal.capitalize())
# Gato Tricolor convierte la primera letra de cada palabra a mayúsculas
print(animal.title())
# GATO TRICOLOR convierte las mayúsculas en minúsculas y viceversa
print(animal.swapcase())
# perro tricolor reemplaza la palabra gato por perro
print(animal.replace("gato", "perro"))
# gato tricolor quitando espacios en blanco antes y después luego es conveniente usar capitalize
print(animal.strip())
# Gato tricolor puedo concatenar métodos de cadenas
print(animal.strip().capitalize())
print(animal.lstrip())  # gato tricolor quitando espacios en blanco a la izquierda
print(animal.rstrip())  # gato tricolor quitando espacios en blanco a la derecha
# 1 nos devuelve la posición de la primera a (índice). Si no encuentra la letra devuelve -1
print(animal.find("a"))
# True nos devuelve True (booleano) si la palabra gato está en la cadena
print("gato" in animal)
# False nos devuelve True (booleano) si la palabra gato no está en la cadena
print("gato" not in animal)
# perro tricolor reemplaza la palabra gato por perro
print(animal.replace("gato", "perro"))


print(len(animal))  # 13 nos devuelve la longitud de la cadena
print(animal.split())  # ['gato', 'tricolor'] devuelve una lista
print(animal.count("a"))  # 2 cuenta la cantidad de veces que aparece la letra a

print(animal.rfind("a"))  # 10 nos devuelve la posición de la última a
print(animal.index("a"))  # 1 nos devuelve la posición de la primera a
print(animal.rindex("a"))  # 10 nos devuelve la posición de la última a
# True nos devuelve True si la cadena empieza con la palabra gato
print(animal.startswith("gato"))
# True nos devuelve True si la cadena termina con la palabra tricolor
print(animal.endswith("tricolor"))
print(animal.isalnum())  # False nos devuelve True si la cadena es alfanumérica
print(animal.isalpha())  # False nos devuelve True si la cadena es alfabética
print(animal.isdigit())  # False nos devuelve True si la cadena es numérica
print(animal.islower())  # True nos devuelve True si la cadena está en minúsculas
