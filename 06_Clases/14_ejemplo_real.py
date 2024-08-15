# Leer, crear, actualizar y eliminar un usuario

class Model:
    table = False  # Atributo de clase que define el nombre de la tabla en la base de datos

    def __init__(self):
        if not self.table:
            print("Error. No se ha definido la tabla")
        else:
            print(f"Trabajando con la tabla {self.table}")

    def guardar(self):
        # Simulación de guardar en la base de datos
        print(f"Guardando {self.table} en la base de datos -BBDD-")

    @classmethod
    def buscar_por_id(cls, _id):
        # Simulación de búsqueda en la base de datos por ID
        print(f"Buscando en la tabla de {
              cls.table} una persona con la id {_id}")


class User(Model):
    table = "usuarios"  # Define la tabla específica para la clase User


# Crear una instancia de User y guardar un usuario
user = User()
user.guardar()  # Salida: Guardando usuarios en la base de datos -BBDD-

# Buscar un usuario por ID
# Salida: Buscando en la tabla de usuarios una persona con la id 3
User.buscar_por_id(3)
