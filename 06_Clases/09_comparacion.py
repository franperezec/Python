# Comparando objetos

# En Python, podemos comparar objetos usando los métodos mágicos __eq__, __ne__, __lt__, __le__, __gt__ y __ge__.
# Estos métodos mágicos nos permiten definir cómo se comparan dos objetos de una clase personalizada.

# A continuación, se muestra un ejemplo de cómo implementar estos métodos para una clase Coordenadas:

class Coordenadas:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    # Método mágico __eq__ para definir el comportamiento del operador de igualdad (==)
    def __eq__(self, other):
        return self.latitud == other.latitud and self.longitud == other.longitud

    # No es necesario definir el método __ne__ (diferente) explícitamente, ya que Python puede derivarlo de __eq__
    # def __ne__(self, other):
    #     return not self == other

    # Método mágico __lt__ para definir el comportamiento del operador "menor que" (<)
    def __lt__(self, other):
        return self.latitud + self.longitud < other.latitud + other.longitud

    # Método mágico __le__ para definir el comportamiento del operador "menor o igual que" (<=)
    def __le__(self, other):
        return self.latitud + self.longitud <= other.latitud + other.longitud


# Crear dos instancias de la clase Coordenadas
coordenada1 = Coordenadas(0, 20)
coordenada2 = Coordenadas(10, 20)

# Antes de definir el método __eq__, al comparar objetos se comparan las direcciones de memoria de los objetos.
# print(coordenada1 == coordenada2)  # Salida: False (esto sucede porque no hemos definido el método __eq__)
# Aquí, se comparan las direcciones de memoria de los objetos coordenada1 y coordenada2, que son diferentes.

# Después de definir el método __eq__, al comparar objetos se comparan los atributos de los objetos.
# Salida: False, porque las coordenadas no son iguales
print(coordenada1 == coordenada2)
# Salida: True, porque las coordenadas no son iguales
print(coordenada1 != coordenada2)
# Salida: True, porque la suma de latitud y longitud de coordenada1 es menor
print(coordenada1 < coordenada2)
# Salida: False, porque coordenada1 no es mayor que coordenada2
print(coordenada1 > coordenada2)
# Salida: True, porque coordenada1 es menor o igual que coordenada2
print(coordenada1 <= coordenada2)

# Imprimir los objetos coordenada1 y coordenada2 muestra sus espacios de memoria
# Salida: <__main__.Coordenadas object at 0x7f4a6e2f4d00> <__main__.Coordenadas object at 0x7f4a6e2f4d30>
print(coordenada1, coordenada2)
# Aquí se muestran las direcciones de memoria (por ejemplo, 0x7f4a6e2f4d00 y 0x7f4a6e2f4d30) de los objetos coordenada1 y coordenada2 respectivamente.
