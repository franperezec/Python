# SQLite es un motor de base de datos ligero que no requiere un servidor para funcionar.
# Esto lo hace ideal para aplicaciones pequeñas y medianas, pruebas de desarrollo, y prototipos.
# SQLite está incluido en la biblioteca estándar de Python, por lo que no es necesario instalar nada adicional.

# Más información sobre SQLite y cómo usarlo en Python se puede encontrar en los siguientes enlaces:
# Documentación oficial de Python: https://docs.python.org/3/library/sqlite3.html
# Sitio web oficial de SQLite: https://www.sqlite.org/index.html
# Tutorial en YouTube sobre SQLite y Python: https://www.youtube.com/watch?v=uUdKAYl-F7g

# Importamos el módulo sqlite3 para trabajar con bases de datos SQLite en Python.
import sqlite3

# Crear una Conexión a la Base de Datos
# -------------------------------------
# Establecemos una conexión a la base de datos "ventas.db", que se almacenará en el directorio "11_BasesDAtos".
# Si el archivo de la base de datos "ventas.db" no existe, SQLite lo creará automáticamente.
# La conexión es necesaria para interactuar con la base de datos (ejecutar consultas, crear tablas, etc.).
conexion = sqlite3.connect('11_BasesDAtos/ventas.db')

# Cerrar la Conexión a la Base de Datos
# -------------------------------------
# Es muy importante cerrar la conexión a la base de datos una vez que termines de trabajar con ella.
# Esto asegura que todos los cambios realizados durante la sesión se guarden correctamente y libera los recursos asociados con la conexión.
conexion.close()
