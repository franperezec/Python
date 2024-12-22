import sqlite3  # Importamos el módulo sqlite3 para trabajar con bases de datos SQLite

# Crear una conexión a la base de datos usando el contexto `with`
# ---------------------------------------------------------------
# Utilizamos `with` para abrir una conexión a la base de datos "ventas.db" ubicada en el directorio "11_BasesDatos".
# Si la base de datos "ventas.db" no existe, SQLite la creará automáticamente.
# El uso de `with` asegura que la conexión se cerrará automáticamente al salir del bloque,
# y cualquier cambio realizado se guardará automáticamente si es necesario.
with sqlite3.connect('11_BasesDatos/ventas.db') as conexion:

    # Crear un cursor para ejecutar sentencias SQL
    # --------------------------------------------
    # Un cursor es un objeto que nos permite interactuar con la base de datos,
    # ejecutar sentencias SQL y recuperar resultados.
    cursor = conexion.cursor()

    # Seleccionar todos los registros de la tabla "productos"
    # -------------------------------------------------------
    # Ejecutamos una sentencia SQL `SELECT * FROM productos` que selecciona todas las columnas de todos los registros
    # en la tabla "productos". El asterisco (`*`) se utiliza como comodín para seleccionar todas las columnas de la tabla.
    cursor.execute('SELECT * FROM productos')

    # Recuperar e imprimir todos los registros del resultado
    # ------------------------------------------------------
    # Utilizamos el método `fetchall()` del cursor para obtener todos los registros resultantes de la consulta.
    # `fetchall()` devuelve una lista de tuplas, donde cada tupla representa un registro de la tabla.
    print(cursor.fetchall())  # Imprime todos los resultados de la consulta
