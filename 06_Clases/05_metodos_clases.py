# Creación de métodos de clase en Python

class Perro:
    # Propiedades de clase (compartidas por todas las instancias)
    especie = "Canis lupus familiaris"
    patas = 4
    cantidad_perros = 0  # Contador de instancias creadas

    def __init__(self, nombre, raza, edad, peso):
        """
        Constructor de la clase Perro.
        Inicializa las propiedades de instancia y actualiza el contador de clase.
        """
        # Propiedades de instancia (únicas para cada instancia)
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

        # Actualizamos la propiedad de clase
        Perro.cantidad_perros += 1

    def comer(self):
        """Simula la acción de comer del perro."""
        return f"{self.nombre} está comiendo."

    def envejecer(self):
        """Incrementa la edad del perro."""
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años."

    @classmethod  # Decorador de método de clase
    def ladrar(cls):  # cls es la convención para referirse a la clase
        """Simula el ladrido del perro."""
        print("Guau, guau!")  # No accedemos a propiedades de instancia ni de clase
    # Factory Method para crear instancias de Perro

    @classmethod
    def factory(cls):
        """Crea una nueva instancia de Perro."""
        return cls("Turco", "Pastor Alemán", 10, 25)


# Ejemplo de uso

Perro.ladrar()  # Salida: Guau, guau!

perro1 = Perro("Firulais", "Labrador", 5, 25)
perro2 = Perro("Rex", "Pastor Alemán", 3, 30)
perro3 = Perro.factory()

print(perro3.nombre, perro3.raza)  # Salida: Turco Pastor Alemán


# perro.py

# class Perro:
#     """
#     Clase que representa a un perro.
#     Demuestra conceptos de POO como propiedades de clase e instancia,
#     métodos de instancia, métodos de clase y factory methods.
#     """

#     # Propiedades de clase (compartidas por todas las instancias)
#     especie = "Canis lupus familiaris"
#     patas = 4
#     cantidad_perros = 0  # Contador de instancias creadas

#     def __init__(self, nombre, raza, edad, peso):
#         """
#         Constructor de la clase Perro.
#         Inicializa las propiedades de instancia y actualiza el contador de clase.

#         :param nombre: Nombre del perro
#         :param raza: Raza del perro
#         :param edad: Edad del perro en años
#         :param peso: Peso del perro en kg
#         """
#         # Propiedades de instancia (únicas para cada instancia)
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad
#         self.peso = peso

#         # Actualizamos la propiedad de clase
#         Perro.cantidad_perros += 1

#     def comer(self):
#         """
#         Simula la acción de comer del perro.
#         :return: String que describe la acción
#         """
#         return f"{self.nombre} está comiendo."

#     def envejecer(self):
#         """
#         Incrementa la edad del perro.
#         :return: String que describe el nuevo estado
#         """
#         self.edad += 1
#         return f"{self.nombre} ahora tiene {self.edad} años."

#     @classmethod
#     def ladrar(cls):
#         """
#         Método de clase que simula el ladrido de un perro.
#         No necesita acceder a propiedades de instancia.
#         """
#         print("Guau, guau!")

#     @classmethod
#     def factory(cls, tipo="default"):
#         """
#         Factory Method para crear instancias de Perro.

#         :param tipo: Tipo de perro a crear (default, pequeño, grande)
#         :return: Nueva instancia de Perro
#         """
#         if tipo == "pequeño":
#             return cls("Fifi", "Chihuahua", 2, 3)
#         elif tipo == "grande":
#             return cls("Rex", "San Bernardo", 4, 50)
#         else:
#             return cls("Turco", "Pastor Alemán", 3, 25)

#     @staticmethod
#     def es_adulto(edad):
#         """
#         Método estático para determinar si un perro es adulto.
#         No necesita acceder a propiedades de clase o instancia.

#         :param edad: Edad del perro
#         :return: Boolean indicando si es adulto
#         """
#         return edad >= 2

#     def __str__(self):
#         """
#         Método especial para representar el objeto como string.
#         :return: String con información del perro
#         """
#         return f"{self.nombre} es un {self.raza} de {self.edad} años y pesa {self.peso} kg"


# # Ejemplo de uso
# if __name__ == "__main__":
#     # Uso del método de clase
#     print("Demostración de ladrido (método de clase):")
#     Perro.ladrar()  # Salida: Guau, guau!

#     # Creación de instancias
#     print("\nCreación de instancias:")
#     perro1 = Perro("Firulais", "Labrador", 5, 25)
#     perro2 = Perro("Luna", "Bulldog", 3, 20)

#     print(perro1)  # Usa el método __str__
#     print(perro2)

#     # Uso de métodos de instancia
#     print("\nUso de métodos de instancia:")
#     print(perro1.comer())
#     print(perro2.envejecer())

#     # Uso del factory method
#     print("\nUso del factory method:")
#     perro3 = Perro.factory("pequeño")
#     perro4 = Perro.factory("grande")
#     print(perro3)
#     print(perro4)

#     # Uso del método estático
#     print("\nUso del método estático:")
#     print(f"¿Es {perro1.nombre} adulto? {Perro.es_adulto(perro1.edad)}")
#     print(f"¿Es {perro3.nombre} adulto? {Perro.es_adulto(perro3.edad)}")

#     # Acceso a propiedades de clase
#     print(f"\nTotal de perros creados: {Perro.cantidad_perros}")
