# Clases en Python: constructor

# Importaciones (si fueran necesarias)
# import math  # Ejemplo de importación, no se usa en este código

# Clase OperacionesMatematicas
class OperacionesMatematicas:
    """
    Esta clase realiza operaciones matemáticas básicas.
    Se usa PascalCase (también conocido como UpperCamelCase) para nombrar la clase.
    """

    def __init__(self, a, b):
        """
        Constructor de la clase OperacionesMatematicas.
        Se llama automáticamente cuando se crea una nueva instancia.

        :param a: Primer número para las operaciones
        :param b: Segundo número para las operaciones
        """
        self.a = a  # Inicializa el atributo 'a'
        self.b = b  # Inicializa el atributo 'b'

    def suma(self):
        """Realiza la suma de los atributos a y b."""
        return self.a + self.b

    def resta(self):
        """Realiza la resta de los atributos a y b."""
        return self.a - self.b

    def multiplicacion(self):
        """Realiza la multiplicación de los atributos a y b."""
        return self.a * self.b

    def division(self):
        """
        Realiza la división de los atributos a y b.
        Nota: Esta función puede causar un error si b es 0.
        """
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero"

# Clase Perro


class Perro:
    """
    Esta clase representa a un perro con atributos y comportamientos básicos.
    """

    def __init__(self, nombre, raza, edad, peso):
        """
        Constructor de la clase Perro.

        :param nombre: Nombre del perro
        :param raza: Raza del perro
        :param edad: Edad del perro en años
        :param peso: Peso del perro en kilogramos
        """
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def ladrar(self):
        """Simula el ladrido del perro."""
        print(f"{self.nombre} dice: Guau, guau!")

    def comer(self):
        """Simula la acción de comer del perro."""
        return f"{self.nombre} está comiendo."

    def dormir(self):
        """Simula la acción de dormir del perro."""
        return f"{self.nombre} está durmiendo."

    def correr(self):
        """Simula la acción de correr del perro."""
        return f"{self.nombre} está corriendo."

    def saltar(self):
        """Simula la acción de saltar del perro."""
        return f"{self.nombre} está saltando."

# Clase Coche


class Coche:
    """
    Esta clase representa a un coche con atributos y comportamientos básicos.
    """

    def __init__(self, marca, modelo, color, precio):
        """
        Constructor de la clase Coche.

        :param marca: Marca del coche
        :param modelo: Modelo del coche
        :param color: Color del coche
        :param precio: Precio del coche
        """
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio

    def arrancar(self):
        """Simula la acción de arrancar el coche."""
        return f"El {self.marca} {self.modelo} está arrancando."

    def acelerar(self):
        """Simula la acción de acelerar el coche."""
        return f"El {self.marca} {self.modelo} está acelerando."

    def frenar(self):
        """Simula la acción de frenar el coche."""
        return f"El {self.marca} {self.modelo} está frenando."

    def girar(self):
        """Simula la acción de girar el coche."""
        return f"El {self.marca} {self.modelo} está girando."

    def apagar(self):
        """Simula la acción de apagar el coche."""
        return f"El {self.marca} {self.modelo} se está apagando."


# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo de uso de OperacionesMatematicas
    operaciones = OperacionesMatematicas(10, 5)
    print(f"Suma: {operaciones.suma()}")
    print(f"Resta: {operaciones.resta()}")
    print(f"Multiplicación: {operaciones.multiplicacion()}")
    print(f"División: {operaciones.division()}")

    # Ejemplo de uso de Perro
    mi_perro = Perro("Rex", "Pastor Alemán", 5, 30)
    mi_perro.ladrar()
    print(mi_perro.comer())
    print(mi_perro.dormir())

    # Ejemplo de uso de Coche
    mi_coche = Coche("Toyota", "Corolla", "Rojo", 25000)
    print(mi_coche.arrancar())
    print(mi_coche.acelerar())
    print(mi_coche.frenar())


# Constructores necesarios para inicializar los atributos de la clase OperacionesMatematicas

# class OperacionesMatematicas:  # se usa PascalCase o UpperCamelCase para el nombre de la clase
#     def __init__(self, a, b):  # constructor de la clase OperacionesMatematicas
#         self.a = a  # inicializa el atributo a
#         self.b = b  # inicializa el atributo b
#     def suma(self, a, b):  # método suma  #self es una referencia al objeto actual de la clase a, b son los parámetros
#         return a + b  # devuelve la suma de a y b

#     def resta(self, a, b):  # método resta
#         return a - b  # devuelve la resta de a y b

#     def multiplicacion(self, a, b):  # método multiplicación
#         return a * b  # devuelve la multiplicación de a y b

#     def division(self, a, b):  # método división
#         return a / b  # devuelve la división de a y b

# class Perro:
#     # constructor de la clase Perro se debe llamar __init__, self es una referencia al objeto actual de la clase, y se puede poner cualquier nombre a los parámetros
#     def __init__(self, nombre, raza, edad, peso):
#         self.nombre = nombre  # inicializa el atributo nombre del objeto
#         self.raza = raza
#         self.edad = edad
#         self.peso = peso

#     def ladrar(self):
#         print(f"{self.nombre} dice: Guau, guau")

#     def comer(self):
#         return "Estoy comiendo"

#     def dormir(self):
#         return "Estoy durmiendo"

#     def correr(self):
#         return "Estoy corriendo"

#     def saltar(self):
#         return "Estoy saltando"


# # instanciación de la clase Perro
# # mi_perro es una instancia de la clase Perro
# mi_perro = Perro("Rex", "Pastor Alemán", 5, 20)
# # mi_perro2 es una instancia de la clase Perro
# mi_perro2 = Perro("Toby", "Labrador", 3, 15)
# mi_perro.ladrar()  # 'Guau, guau'
# print(mi_perro.nombre)
# print(mi_perro2.nombre)
# class Coche:
#     def __init__(self, marca, modelo, color, precio):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.precio = precio
#     def arrancar(self):
#         return "Estoy arrancando"
#     def acelerar(self):
#         return "Estoy acelerando"
#     def frenar(self):
#         return "Estoy frenando"
#     def girar(self):
#         return "Estoy girando"
#     def apagar(self):
#         return "Estoy apagando"
