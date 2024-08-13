# Alcance de las variables
# Las variables aún con el mismo nombre pueden tener valores diferentes si se encuentran en funciones diferentes
# variables locales: Son las que se declaran dentro de una función y no son accesibles desde fuera de la función
# variables globales: Son las que se declaran fuera de una función y son accesibles desde cualquier lugar del código
# Ejemplo de variables locales
# def saludar():
#     nombre = "Juan"
#     print(f"Hola {nombre}")
#
# def saludar2():
#     nombre = "Karla"
#     print(f"Hola {nombre}")
#
# saludar()
# saludar2()
# En este ejemplo, la variable nombre es local a cada función, por lo que no se puede acceder a ella desde fuera de la función.
# Ejemplo de variables globales
# nombre = "Francisco"

# Variables globales
# Es debatible si usar variables globales es una buena práctica
nombre_global = "Francisco"

# Ejemplo de variables locales


def saludar_local():
    nombre = "Juan"  # Variable local
    print(f"Hola {nombre}")


def saludar_local2():
    nombre = "Karla"  # Variable local, diferente a la de saludar_local
    print(f"Hola {nombre}")

# Funciones que usan la variable global


def saludar_global():
    print(f"Hola {nombre_global}")


def modificar_global():
    global nombre_global
    nombre_global = "Eduardo"


# Demostración de uso
print("--- Demostración de variables locales ---")
saludar_local()
saludar_local2()

print("\n--- Demostración de variable global ---")
print(f"Valor inicial de nombre_global: {nombre_global}")
saludar_global()
modificar_global()
print(f"Valor de nombre_global después de modificar_global(): {nombre_global}")

# Nota: El siguiente código causaría un error y ha sido comentado
# resultado1 = modificar_global() + 3
# print(resultado1)

print("\n--- Demostración de error potencial ---")
try:
    resultado2 = nombre_global + 3
    print(resultado2)
except TypeError as e:
    print(f"Error: {e}")
    print("No se puede sumar un string con un número.")

print(f"\nValor final de nombre_global: {nombre_global}")
