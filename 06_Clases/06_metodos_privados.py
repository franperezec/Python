# Propiedades privadas, métodos get y set

# Por ejemplo el nombre de un perro no debería ser modificado directamente, sino a través de un método que valide la nueva cadena.

class Perro:

    def __init__(self, nombre, raza, edad, peso):
        """
        Constructor de la clase Perro.
        Inicializa las propiedades de instancia y actualiza el contador de clase.
        """
        # Propiedades de instancia (únicas para cada instancia)
        # Propiedad privada Shif +Ctrl + P en nombre y seleccionar "Rename Symbol" cambiar y Enter
        self.__nombre = nombre
        self.raza = raza    # Propiedad pública
        self.edad = edad
        self.peso = peso

    # podemos leer el nombre pero no modificarlo

    def get_nombre(self):
        return self.__nombre

    # podemos modificar el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def comer(self):
        """Simula la acción de comer del perro."""
        return f"{self.__nombre} está comiendo."

    def envejecer(self):
        """Incrementa la edad del perro."""
        self.edad += 1
        return f"{self.__nombre} ahora tiene {self.edad} años."

    def ladrar(self):  # cls es la convención para referirse a la clase
        """Simula el ladrido del perro."""
        print(
            # No accedemos a propiedades de instancia ni de clase
            f"{self.__nombre} dice: Guau, guau!")
    # Factory Method para crear instancias de Perro

    @classmethod
    def factory(cls):
        """Crea una nueva instancia de Perro."""
        return cls("Turco", "Pastor Alemán", 10, 25)


# Ejemplo de uso

perro1 = Perro.factory()
perro1.ladrar()  # Salida: Guau, guau! #aaceso dentro de la misma clase

# AttributeError: 'Perro' object has no attribute '__nombre' #no se puede acceder a la propiedad privada desde fuera de la clase
# print(perro1.__nombre)

# con método get_nombre puedo leer el nombre
print(perro1.get_nombre())

# propiedasdes de la instancia de un objeto

# {'_Perro__nombre': 'Turco', 'raza': 'Pastor Alemán', 'edad': 10, 'peso': 25}
print(perro1.__dict__)

# podemos copiar el objeto _Perro__nombre pero es una mala práctica

print(perro1._Perro__nombre)  # Turco


# # perro.py

# class Perro:
#     """
#     Clase que representa a un perro.
#     Demuestra el uso de propiedades privadas y métodos getter/setter.
#     """

#     # Variable de clase para contar la cantidad de perros creados
#     cantidad_perros = 0

#     def __init__(self, nombre, raza, edad, peso):
#         """
#         Constructor de la clase Perro.
#         Inicializa las propiedades de instancia y actualiza el contador de clase.

#         :param nombre: Nombre del perro (str)
#         :param raza: Raza del perro (str)
#         :param edad: Edad del perro en años (int)
#         :param peso: Peso del perro en kg (float)
#         """
#         # Propiedades privadas
#         self.__nombre = nombre
#         self.__raza = raza
#         self.__edad = edad
#         self.__peso = peso

#         # Incrementamos el contador de perros
#         Perro.cantidad_perros += 1

#     # Métodos getter
#     def get_nombre(self):
#         """Obtiene el nombre del perro."""
#         return self.__nombre

#     def get_raza(self):
#         """Obtiene la raza del perro."""
#         return self.__raza

#     def get_edad(self):
#         """Obtiene la edad del perro."""
#         return self.__edad

#     def get_peso(self):
#         """Obtiene el peso del perro."""
#         return self.__peso

#     # Métodos setter con validación
#     def set_nombre(self, nombre):
#         """
#         Establece el nombre del perro.

#         :param nombre: Nuevo nombre (str)
#         """
#         if isinstance(nombre, str) and len(nombre) > 0:
#             self.__nombre = nombre
#         else:
#             raise ValueError("El nombre debe ser una cadena no vacía.")

#     def set_raza(self, raza):
#         """
#         Establece la raza del perro.

#         :param raza: Nueva raza (str)
#         """
#         if isinstance(raza, str) and len(raza) > 0:
#             self.__raza = raza
#         else:
#             raise ValueError("La raza debe ser una cadena no vacía.")

#     def set_edad(self, edad):
#         """
#         Establece la edad del perro.

#         :param edad: Nueva edad (int)
#         """
#         if isinstance(edad, int) and edad >= 0:
#             self.__edad = edad
#         else:
#             raise ValueError("La edad debe ser un entero no negativo.")

#     def set_peso(self, peso):
#         """
#         Establece el peso del perro.

#         :param peso: Nuevo peso (float)
#         """
#         if isinstance(peso, (int, float)) and peso > 0:
#             self.__peso = peso
#         else:
#             raise ValueError("El peso debe ser un número positivo.")

#     def comer(self):
#         """Simula la acción de comer del perro."""
#         return f"{self.__nombre} está comiendo."

#     def envejecer(self):
#         """Incrementa la edad del perro."""
#         self.__edad += 1
#         return f"{self.__nombre} ahora tiene {self.__edad} años."

#     def ladrar(self):
#         """Simula el ladrido del perro."""
#         print(f"{self.__nombre} dice: Guau, guau!")

#     @classmethod
#     def factory(cls):
#         """
#         Factory Method para crear instancias de Perro.
#         :return: Nueva instancia de Perro
#         """
#         return cls("Turco", "Pastor Alemán", 10, 25)

#     def __str__(self):
#         """Representación en string del perro."""
#         return f"{self.__nombre} es un {self.__raza} de {self.__edad} años y pesa {self.__peso} kg"


# # Ejemplo de uso
# if __name__ == "__main__":
#     print("Creando un perro usando el factory method:")
#     perro1 = Perro.factory()
#     perro1.ladrar()

#     print("\nAccediendo a propiedades usando getters:")
#     print(f"Nombre: {perro1.get_nombre()}")
#     print(f"Raza: {perro1.get_raza()}")
#     print(f"Edad: {perro1.get_edad()}")
#     print(f"Peso: {perro1.get_peso()}")

#     print("\nModificando propiedades usando setters:")
#     perro1.set_nombre("Rex")
#     perro1.set_edad(5)
#     print(perro1)  # Usa el método __str__

#     print("\nIntentando acceder directamente a una propiedad privada:")
#     try:
#         print(perro1.__nombre)
#     except AttributeError as e:
#         print(f"Error: {e}")

#     print("\nAccediendo a la propiedad privada nombre usando name mangling:")
#     print(perro1._Perro__nombre)

#     print("\nMostrando todas las propiedades de la instancia:")
#     print(perro1.__dict__)

#     print(f"\nTotal de perros creados: {Perro.cantidad_perros}")
