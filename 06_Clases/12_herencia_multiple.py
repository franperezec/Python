# Herencia múltiple en Python

# En la herencia múltiple, podemos heredar de más de una clase base.
# Esto es útil para reutilizar código y evitar duplicación, pero puede
# volverse complicado si no se maneja con cuidado.

class Animal:
    # Método de la clase base Animal
    def comer(self):
        print("¡Estoy comiendo!")


class Perro:
    # Método específico de la clase Perro
    def pasear(self):
        print("¡Estoy paseando al perro!")

# Gato hereda de Perro y Animal. En caso de que ambas clases tuvieran un método
# con el mismo nombre, se ejecutará el método de la clase que esté más a la izquierda en la lista de herencia.


class Gato(Perro, Animal):  # Herencia múltiple: hereda de Perro y Animal
    # Método específico de la clase derivada Gato
    def maullar(self):
        print("¡Miau, miau!")


# Crear una instancia de Gato
gato = Gato()
gato.maullar()   # Salida: ¡Miau, miau!
gato.pasear()    # Salida: ¡Estoy paseando al perro! (Hereda de Perro)
gato.comer()     # Salida: ¡Estoy comiendo! (Hereda de Animal)

# Otro ejemplo: evitando la duplicación de código con herencia múltiple


class Caminar:
    def caminar(self):
        print("¡Estoy caminando!")


class Nadar:
    def nadar(self):
        print("¡Estoy nadando!")


class Volar:
    def volar(self):
        print("¡Estoy volando!")

# Pato hereda de Caminar, Nadar, y Volar, reutilizando los métodos de esas clases


class Pato(Caminar, Nadar, Volar):
    def graznar(self):
        print("¡Cuac, cuac!")


# Crear una instancia de Pato
pato = Pato()
pato.caminar()   # Salida: ¡Estoy caminando! (Hereda de Caminar)
pato.nadar()     # Salida: ¡Estoy nadando! (Hereda de Nadar)
pato.volar()     # Salida: ¡Estoy volando! (Hereda de Volar)
pato.graznar()   # Salida: ¡Cuac, cuac! (Método específico de Pato)
