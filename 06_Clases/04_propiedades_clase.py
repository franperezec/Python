# Clases en Python: Propiedades de Clase y Propiedades de Instancia

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

    def ladrar(self):
        """Simula el ladrido del perro."""
        print(f"{self.nombre} dice: Guau, guau!")

    def comer(self):
        """Simula la acción de comer del perro."""
        return f"{self.nombre} está comiendo."

    def envejecer(self):
        """Incrementa la edad del perro."""
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años."

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        """
        Método de clase para cambiar la especie de todos los perros.
        """
        cls.especie = nueva_especie

    @staticmethod
    def es_adulto(edad):
        """
        Método estático para determinar si un perro es adulto.
        No necesita acceder a propiedades de instancia ni de clase.
        """
        return edad >= 3


# Ejemplos de uso
if __name__ == "__main__":
    # Creamos instancias de Perro
    firulais = Perro("Firulais", "Labrador", 5, 25)
    rex = Perro("Rex", "Pastor Alemán", 3, 30)

    # Accedemos a propiedades de clase
    print(f"Todos los perros tienen {Perro.patas} patas.")
    print(f"La especie de todos los perros es: {Perro.especie}")
    print(f"Cantidad de perros creados: {Perro.cantidad_perros}")

    # Accedemos a propiedades de instancia
    print(f"{firulais.nombre} es un {firulais.raza} de {
          firulais.edad} años y pesa {firulais.peso} kg.")
    print(f"{rex.nombre} es un {rex.raza} de {
          rex.edad} años y pesa {rex.peso} kg.")

    # Usamos métodos de instancia
    firulais.ladrar()
    print(rex.comer())
    print(firulais.envejecer())

    # Usamos un método de clase para cambiar una propiedad de clase
    Perro.cambiar_especie("Canis lupus")
    print(f"Ahora la especie de todos los perros es: {Perro.especie}")

    # Usamos un método estático
    print(f"¿Es Firulais adulto? {Perro.es_adulto(firulais.edad)}")
    print(f"¿Es un perro de 2 años adulto? {Perro.es_adulto(2)}")

    # Demostramos que cambiar una propiedad de instancia no afecta a otras instancias
    firulais.patas = 3
    print(f"{firulais.nombre} ahora tiene {firulais.patas} patas (accidente).")
    print(f"Pero {rex.nombre} aún tiene {rex.patas} patas.")
    print(f"Y la clase Perro sigue diciendo que los perros tienen {
          Perro.patas} patas.")
