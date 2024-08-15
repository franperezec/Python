# Decorador @property

# En Python, los métodos de instancia pueden ser decorados con el decorador @property.

# Este decorador convierte un método en una propiedad de solo lectura. Es decir, permite acceder a un método como si fuera un atributo, sin necesidad de usar paréntesis.

# Para definir una propiedad, se debe usar el decorador @property antes de la definición del método. A continuación, se muestra un ejemplo:

# class Perro:
#     def __init__(self, nombre):
#         self.set_nombre(nombre)

#     def set_nombre(self, nombre):
#         if nombre.strip():
#             self.__nombre = nombre  # El atributo es privado
#         return self.__nombre

#     def get_nombre(self):
#         return self.__nombre


# perro = Perro("Firulais")
# print(perro.get_nombre())  # Salida: Firulais


# vamos a mejorar el código anterior se muestran tres alternativas para definir una propiedad en una clase ahora

# Ejemplo de uso del decorador @property en Python

# El decorador @property permite transformar un método de instancia en una propiedad de solo lectura.
# Esto significa que podemos acceder a un método como si fuera un atributo, sin usar paréntesis.

# A continuación, se muestra un ejemplo básico para explicar cómo funciona @property:

class Perro:
    def __init__(self, nombre):
        # Aquí se llama al setter de 'nombre' durante la inicialización
        self.nombre = nombre

    # El decorador @property transforma el método en una propiedad (getter)
    @property
    def nombre(self):
        print("Accediendo al getter de 'nombre'")
        return self.__nombre

    # El decorador @nombre.setter define un setter para la propiedad 'nombre'
    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por el setter de 'nombre'")
        # Validamos que el nombre no sea una cadena vacía o espacios en blanco
        if nombre.strip():
            self.__nombre = nombre  # Guardamos el valor en un atributo privado
        else:
            raise ValueError("El nombre no puede estar vacío")

    # Al usar los decoradores, podemos controlar cómo se accede y modifica el valor de 'nombre'.
    # Esto ayuda a encapsular y proteger los datos dentro de la clase.


# Ejemplo de uso:
perro = Perro("Firulais")
# Salida esperada: 'Accediendo al getter de 'nombre'' y 'Firulais'
print(perro.nombre)

# Intentar modificar el nombre:
perro.nombre = "Rex"
print(perro.nombre)  # Salida esperada: 'Accediendo al getter de 'nombre'' y 'Rex'
