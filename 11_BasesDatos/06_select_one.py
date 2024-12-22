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
    # Utilizamos la sentencia SQL `SELECT * FROM productos` para seleccionar todas las columnas de todos los registros
    # en la tabla "productos". El asterisco (`*`) indica que se seleccionarán todas las columnas.
    cursor.execute('SELECT * FROM productos')

    # Recuperar e imprimir el primer registro del resultado
    # -----------------------------------------------------
    # Utilizamos el método `fetchone()` del cursor para obtener el primer registro del conjunto de resultados de la consulta.
    # `fetchone()` devuelve una tupla que contiene los valores del primer registro.
    # Si no hay más registros disponibles, `fetchone()` devuelve `None`.
    print(cursor.fetchone())  # Imprime el primer resultado de la consulta
