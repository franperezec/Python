# Importamos el módulo sqlite3, que nos permite trabajar con bases de datos SQLite en Python.
import sqlite3

# Crear una conexión a la base de datos
# -------------------------------------
# `sqlite3.connect()` establece una conexión con la base de datos especificada.
# Si el archivo 'ventas.db' no existe, SQLite lo crea automáticamente.
# Aquí, estamos creando o conectándonos a una base de datos llamada 'ventas.db',
# que se almacenará en el directorio '11_BasesDatos'.
conexion = sqlite3.connect('11_BasesDatos/ventas.db')

# Crear un cursor para ejecutar sentencias SQL
# --------------------------------------------
# Un cursor es un objeto que nos permite interactuar con la base de datos.
# Podemos utilizarlo para ejecutar sentencias SQL y recuperar resultados.
cursor = conexion.cursor()

# Crear una tabla en la base de datos
# -----------------------------------
# Aquí utilizamos el cursor para ejecutar una sentencia SQL que crea una tabla llamada "productos".
# Esta tabla tendrá tres columnas: `id`, `nombre`, y `precio`.
# - `id INTEGER PRIMARY KEY`: Esto define una columna `id` que será la clave primaria,
#   lo que significa que cada valor en esta columna será único y no nulo.
# - `nombre VARCHAR(100)`: Esto define una columna `nombre` que almacenará cadenas de texto de hasta 100 caracteres.
# - `precio FLOAT`: Esto define una columna `precio` que almacenará números decimales.
# La cláusula `IF NOT EXISTS` asegura que la tabla solo se creará si no existe ya en la base de datos.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(100),
        precio FLOAT
    )
''')  # Ejecutamos la sentencia SQL para crear la tabla.

# Guardar los cambios en la base de datos
# ---------------------------------------
# `conexion.commit()` es necesario para confirmar los cambios realizados en la base de datos.
# Sin esta línea, los cambios no se guardarían permanentemente.
# Esto asegura que la tabla se cree y que cualquier otro cambio realizado en la base de datos
# durante esta sesión se guarde correctamente.
conexion.commit()

# Cerrar la conexión a la base de datos
# -------------------------------------
# Siempre es importante cerrar la conexión a la base de datos cuando se termina de trabajar con ella.
# Esto libera los recursos y asegura que todos los cambios se guarden.
conexion.close()

# Nota adicional:
# Puedes ver y manipular la base de datos usando el comando `sqlite3 ventas.db` en la terminal.
# También puedes instalar un gestor de base de datos gráfico como DB Browser for SQLite,
# que facilita la visualización y edición de la base de datos.
