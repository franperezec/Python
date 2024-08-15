# Polimorfismo en Python

from abc import ABC, abstractmethod

# Definición de la clase abstracta Model


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

# Clase User que hereda de Model


class User(Model):
    # Implementación del método guardar para User
    def guardar(self):
        print("Guardando usuario en la base de datos")

# Clase Session que hereda de Model, identifica una sesión de usuario


class Session(Model):
    # Implementación del método guardar para Session
    def guardar(self):
        print("Guardando sesión en archivo de texto")

# Función guardar que demuestra el polimorfismo


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()  # Se llama al método guardar específico de cada objeto


# Crear instancias de User y Session
usuario = User()
sesion = Session()

# Polimorfismo: se ejecuta el método guardar de cada clase para ahorrar código
guardar([sesion, usuario])
# Salida:
# Guardando sesión en archivo de texto
# Guardando usuario en la base de datos

# Ambas clases tienen un método guardar, pero con implementaciones diferentes.
# El polimorfismo permite que el mismo código (en la función guardar) pueda manejar diferentes tipos de objetos de manera uniforme.

# # ==============================================================

# # Polimorfismo en Python
# # ======================
# # El polimorfismo es un concepto clave en la Programación Orientada a Objetos (OOP), que permite que una misma
# # operación o método se aplique a objetos de diferentes clases. Este principio es fundamental para escribir
# # código que sea extensible, flexible y reutilizable, ya que permite manejar diferentes tipos de objetos
# # de manera uniforme.

# # Importamos ABC y abstractmethod desde el módulo abc. Estas herramientas nos permiten definir clases abstractas,
# # que son clases que no se pueden instanciar y que usualmente contienen métodos abstractos. Un método abstracto
# # es un método que no tiene implementación en la clase base, y que debe ser implementado en cualquier clase derivada.

# from abc import ABC, abstractmethod

# # Definición de la clase abstracta `Model`
# # ----------------------------------------
# # La clase `Model` es una clase base abstracta. En este contexto, actúa como una interfaz que define un contrato
# # que deben cumplir todas las clases que hereden de ella. Este contrato se expresa a través del método abstracto
# # `guardar()`, el cual todas las clases derivadas deben implementar.

# class Model(ABC):
#     @abstractmethod
#     def guardar(self):
#         """
#         Método abstracto que debe ser implementado por cualquier clase que herede de `Model`.
#         Esta es una plantilla que asegura que cualquier clase hija tendrá un método `guardar`.
#         """
#         pass

# # Clase `User` que hereda de `Model`
# # ----------------------------------
# # Esta es una clase concreta que representa un usuario en el sistema. Hereda de `Model` y, por lo tanto, está
# # obligada a implementar el método `guardar`. Aquí se define que guardar un usuario implica "almacenarlo en una
# # base de datos". Este es un ejemplo de cómo una clase concreta cumple el contrato definido por la clase abstracta.

# class User(Model):
#     def guardar(self):
#         """
#         Implementación concreta del método `guardar` para la clase `User`.
#         Simula la acción de guardar un usuario en una base de datos.
#         """
#         print("Guardando usuario en la base de datos")

# # Clase `Session` que hereda de `Model`
# # -------------------------------------
# # Similar a la clase `User`, `Session` es una clase concreta que representa una sesión de usuario. También hereda
# # de `Model` y, por lo tanto, debe implementar el método `guardar`. Sin embargo, en este caso, guardar una sesión
# # significa "almacenarla en un archivo de texto". Esto muestra cómo diferentes clases pueden implementar el mismo
# # método de manera distinta según el contexto de cada clase.

# class Session(Model):
#     def guardar(self):
#         """
#         Implementación concreta del método `guardar` para la clase `Session`.
#         Simula la acción de guardar una sesión en un archivo de texto.
#         """
#         print("Guardando sesión en archivo de texto")

# # Función `guardar`
# # -----------------
# # Esta función es un ejemplo clásico de polimorfismo. Recibe una lista de objetos, donde se espera que todos
# # implementen el método `guardar`. La función itera sobre la lista y llama al método `guardar` en cada objeto,
# # sin necesidad de conocer el tipo específico del objeto. El polimorfismo asegura que el método correcto será
# # llamado para cada objeto según su clase.

# def guardar(entidades):
#     """
#     Función que recibe una lista de objetos y llama al método `guardar` de cada uno.
#     Esta función es polimórfica: no necesita saber el tipo específico de los objetos en la lista,
#     solo requiere que estos objetos implementen el método `guardar`.
#     """
#     for entidad in entidades:
#         entidad.guardar()

# # Ejecución del código
# # --------------------
# # Aquí creamos instancias de `User` y `Session`. Luego, usamos la función `guardar` para guardar tanto un usuario
# # como una sesión. A través del polimorfismo, la misma función puede manejar diferentes tipos de objetos de manera
# # uniforme y ejecutar el método correcto en cada caso.

# # Crear una instancia de `User`
# usuario = User()

# # Crear una instancia de `Session`
# sesion = Session()

# # Usar la función `guardar` para ambos objetos
# # --------------------------------------------
# # Al pasar una lista con las instancias `usuario` y `sesion` a la función `guardar`, demostramos cómo
# # el polimorfismo permite que la misma función trate ambos objetos, llamando al método `guardar` apropiado
# # según el tipo del objeto.

# guardar([sesion, usuario])
# # Salida esperada:
# # Guardando sesión en archivo de texto
# # Guardando usuario en la base de datos

# # Análisis del Polimorfismo en este Ejemplo
# # -----------------------------------------
# # Este ejemplo ilustra cómo el polimorfismo nos permite escribir código más general y flexible.
# # La función `guardar` no necesita preocuparse por qué tipo de objeto está procesando; simplemente
# # llama al método `guardar` de cada objeto, y gracias al polimorfismo, el método correcto es invocado.
# # Esto facilita la extensión del código para soportar nuevos tipos de objetos en el futuro, sin modificar
# # la lógica existente.
