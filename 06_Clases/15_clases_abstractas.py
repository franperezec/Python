# Clases abstractas

# Importar ABC y abstractmethod de la librería abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definición de la clase abstracta Model


class Model(ABC):

    # Propiedad abstracta que debe ser implementada por cualquier clase derivada
    @property
    @abstractmethod
    def table(self):
        pass

    # Método abstracto que debe ser implementado por cualquier clase derivada
    @abstractmethod
    def guardar(self):
        pass

    # Método de clase que no es abstracto, pero puede ser utilizado en clases derivadas
    @classmethod
    def buscar_por_id(cls, _id):
        # Simulación de búsqueda en la base de datos por ID
        print(f"Buscando en la tabla de {
              cls.table} una persona con la id {_id}")

# Definición de la clase User que hereda de Model


class User(Model):
    table = "usuarios"  # Define la tabla específica para la clase User

    # Implementación del método abstracto guardar
    def guardar(self):
        # Simulación de guardar en la base de datos
        print(f"Guardando {self.table} en la base de datos -BBDD-")


# Crear una instancia de User y guardar un usuario
user = User()
user.guardar()  # Salida: Guardando usuarios en la base de datos -BBDD-

# Buscar un usuario por ID
# Salida: Buscando en la tabla de usuarios una persona con la id 3
User.buscar_por_id(3)

# Si intentamos crear una instancia de la clase Model, obtendremos un error
# model = Model()
# TypeError: Can't instantiate abstract class Model with abstract methods guardar, table
