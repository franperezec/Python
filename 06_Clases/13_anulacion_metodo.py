# Anulación de método o Method Overriding

class Ave:  # Clase base o padre
    def __init__(self):
        self.vuela = True

    # Método volar de la clase base
    def volar(self):
        print("¡Estoy volando soy un ave!")


class Pato(Ave):  # Clase derivada o hija que hereda de Ave pero anula el método volar
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base (Ave)
        self.nada = True

    # Método volar anulado en la clase derivada
    def volar(self):
        print("¡Estoy volando soy un pato!")
        super().volar()  # Llama al método volar de la clase base


# Crear una instancia de Pato
pato = Pato()

# Llamar al método volar anulado en la instancia de Pato
pato.volar()  # Salida: ¡Estoy volando soy un pato! ¡Estoy volando soy un ave!

# Imprimir los atributos de la instancia de Pato
print(pato.vuela, pato.nada)  # Salida: True True
