# Métodos mágicos

# En Python, los métodos mágicos son métodos especiales que tienen doble guion bajo
# al principio y al final de su nombre. Estos métodos son llamados automáticamente
# por el intérprete de Python en situaciones específicas.

# Los métodos mágicos nos permiten definir comportamientos personalizados para
# nuestras clases. Por ejemplo, podemos definir cómo se suman dos objetos.

# Para definir un método mágico, simplemente debemos implementar un método con
# el nombre correspondiente en nuestra clase. A continuación, se muestra un
# ejemplo con algunos de los métodos mágicos más comunes en Python:

class Perro:
    # Método constructor o mágico por defecto __init__, __new__, __del__, ...
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método mágico __del__ para definir el comportamiento al eliminar un objeto
    def __del__(self):
        print(f"El perro {self.nombre} ha sido eliminado")

    # Método mágico __str__ para definir la representación del objeto como string
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

    # Método regular (no mágico) para hacer que el perro ladre
    def ladra(self):
        print(f"{self.nombre} dice: ¡Guau, guau!")


# Crear una instancia de la clase Perro
perro = Perro("Firulais", 5)
perro2 = Perro("Rex", 3)

# Llamada al método mágico __del__ al eliminar el objeto
del perro2

# Llamada al método regular ladra
perro.ladra()  # Salida: Firulais dice: ¡Guau, guau!"

# El método __dict__ devuelve un diccionario con los atributos de la instancia
# Salida: {'nombre': 'Firulais', 'edad': 5}
print(perro.__dict__)

# Al imprimir el objeto, se llama al método mágico __str__
# Salida: Firulais (5 años)
print(perro)

# Este código es equivalente a la línea anterior
# Convertir el objeto a string usando el método __str__
texto = str(perro)
print(texto)  # Salida: Firulais (5 años)

# Para más información sobre los métodos mágicos:
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# https://realpython.com/python-magic-methods/#arithmetic-operators
# https://rszalski.github.io/magicmethods/
# https://www.geeksforgeeks.org/dunder-magic-methods-python/
