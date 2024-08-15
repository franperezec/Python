# Herencia en Python

class Animal:
    # Método de la clase base Animal
    def comer(self):
        print("¡Estoy comiendo!")


class Perro(Animal):  # Hereda de la clase Animal (Herencia simple)
    # Método específico de la clase derivada Perro
    def pasear(self):
        print("¡Estoy paseando!")


class Gato(Perro):  # Hereda de la clase Perro (Herencia múltiple)
    # Método específico de la clase derivada Gato
    def maullar(self):
        print("¡Miau, miau!")


# Crear una instancia de la clase Perro
perro = Perro()
perro.pasear()  # Salida: ¡Estoy paseando!

# Crear una instancia de la clase Gato
gato = Gato()
gato.pasear()  # Salida: ¡Estoy paseando! (Hereda este método de Perro)

# Corregir la llamada al método pasear para Gato
gato.pasear()  # Llama al método pasear heredado de Perro
gato.maullar()  # Salida: ¡Miau, miau! (Método específico de Gato)
gato.comer()  # Salida: ¡Estoy comiendo! (Método heredado de Animal)
