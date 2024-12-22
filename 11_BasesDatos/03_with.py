# Importamos el módulo sqlite3, que nos permite trabajar con bases de datos SQLite en Python.
import sqlite3

# Crear una conexión a la base de datos usando el contexto `with`
# ---------------------------------------------------------------
# Utilizamos `with` para abrir una conexión a la base de datos "ventas.db" ubicada en el directorio "11_BasesDatos".
# Si la base de datos no existe, SQLite la creará automáticamente.
# El uso de `with` garantiza que la conexión se cerrará automáticamente cuando se salga del bloque `with`,
# y también se realizará un commit automáticamente si se han realizado cambios en la base de datos.
with sqlite3.connect('11_BasesDatos/ventas.db') as conexion:

    # Crear un cursor para ejecutar sentencias SQL
    # --------------------------------------------
    # Un cursor es un objeto que nos permite interactuar con la base de datos,
    # ejecutar sentencias SQL y recuperar resultados.
    cursor = conexion.cursor()

    # Crear una tabla en la base de datos
    # -----------------------------------
    # Usamos el cursor para ejecutar una sentencia SQL que crea una tabla llamada "productos".
    # La tabla tendrá las siguientes columnas:
    # - id: un identificador único para cada producto (clave primaria), que es de tipo INTEGER.
    # - nombre: una columna para almacenar el nombre del producto, que es de tipo VARCHAR y puede contener hasta 100 caracteres.
    # - precio: una columna para almacenar el precio del producto, que es de tipo FLOAT.
    # La cláusula `IF NOT EXISTS` asegura que la tabla solo se creará si no existe ya en la base de datos,
    # evitando errores si la tabla ya existe.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(100),
            precio FLOAT
        )
    ''')  # Ejecutamos la sentencia SQL para crear la tabla.
