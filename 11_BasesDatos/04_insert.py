import sqlite3  # Importamos el módulo sqlite3 para trabajar con bases de datos SQLite

# Crear una conexión a la base de datos usando el contexto `with`
# ---------------------------------------------------------------
# Utilizamos `with` para abrir una conexión a la base de datos "ventas.db" ubicada en el directorio "11_BasesDatos".
# Si el archivo de la base de datos "ventas.db" no existe, SQLite lo creará automáticamente.
# El uso de `with` garantiza que la conexión se cerrará automáticamente cuando se salga del bloque `with`,
# y también se realizará un commit automáticamente si se han realizado cambios en la base de datos.
with sqlite3.connect('11_BasesDatos/ventas.db') as conexion:

    # Crear un cursor para ejecutar sentencias SQL
    # --------------------------------------------
    # El cursor es un objeto que nos permite interactuar con la base de datos,
    # ejecutar sentencias SQL y recuperar resultados.
    cursor = conexion.cursor()

    # Insertar datos en la tabla "productos"
    # --------------------------------------
    # Usamos la sentencia SQL `INSERT INTO` para agregar un nuevo registro en la tabla "productos".
    # Los valores a insertar son: id = 1, nombre = "Teclado", precio = 20.0.
    # La sintaxis `?` se utiliza como marcadores de posición para los valores que se van a insertar.
    # Estos marcadores serán reemplazados por los valores que se pasan como segundo argumento en la tupla `(1, "Teclado", 20.0)`.
    # Este método de insertar datos previene inyecciones SQL, ya que los valores son tratados como datos y no como parte del código SQL.
    cursor.execute(
        "INSERT INTO productos VALUES(?, ?, ?)",
        (1, "Teclado", 20.0)
    )
