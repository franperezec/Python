import sqlite3  # Importamos el módulo sqlite3 para trabajar con bases de datos SQLite

# Crear una conexión a la base de datos usando el contexto `with`
# ---------------------------------------------------------------
# Utilizamos `with` para abrir una conexión a la base de datos "ventas.db" ubicada en el directorio "11_BasesDatos".
# Si el archivo de la base de datos "ventas.db" no existe, SQLite lo creará automáticamente.
# El uso de `with` asegura que la conexión se cerrará automáticamente al final del bloque,
# y cualquier cambio realizado se guardará automáticamente.
with sqlite3.connect('11_BasesDatos/ventas.db') as conexion:

    # Crear un cursor para ejecutar sentencias SQL
    # --------------------------------------------
    # Un cursor es un objeto que nos permite interactuar con la base de datos,
    # ejecutar sentencias SQL y obtener resultados.
    cursor = conexion.cursor()

    # Lista de productos a insertar en la tabla
    # -----------------------------------------
    # Creamos una lista de tuplas, donde cada tupla representa un producto que queremos insertar en la tabla "productos".
    # Cada tupla contiene los valores: id, nombre y precio.
    productos = [
        (2, "Ratón", 10.0),
        (3, "Monitor", 200.0),
        (4, "Impresora", 150.0),
    ]

    # Inserción múltiple de registros en la tabla "productos"
    # ------------------------------------------------------
    # Utilizamos la función `executemany()` para insertar varios registros en la tabla "productos" de una sola vez.
    # La sentencia SQL `INSERT INTO productos VALUES(?, ?, ?)` se aplica a cada tupla en la lista `productos`.
    # Los `?` son marcadores de posición que serán reemplazados por los valores de cada tupla en la lista.
    # Esto asegura que los valores se inserten de manera segura y eficiente, evitando inyecciones SQL.
    cursor.executemany(
        "INSERT INTO productos VALUES(?, ?, ?)",
        productos
    )
