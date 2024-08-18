# Trabajando con Archivos en Python usando la función open
# ========================================================
# En este ejemplo, aprenderemos a leer, escribir y modificar archivos utilizando la función open de Python.
# Esta función es fundamental para manejar archivos y permite realizar varias operaciones según el modo en que se abra el archivo.

# Importamos la función open desde el módulo io para trabajar con archivos
from io import open

# Escritura en un Archivo
# -----------------------
# Aquí escribiremos un texto en un archivo utilizando el modo "w" (write). Si el archivo no existe, Python lo crea automáticamente.
texto = "Hola, vamos a ganar"

# Abrimos el archivo en modo escritura. Si el archivo "prueba.txt" no existe, se creará.
archivo = open("10_Archivos/prueba.txt", "w")

# Escribimos el texto en el archivo
archivo.write(texto)

# Cerramos el archivo para liberar los recursos y asegurarnos de que los cambios se guarden correctamente.
archivo.close()

# Lectura de un Archivo
# ---------------------
# Ahora, leeremos el contenido del archivo que acabamos de escribir utilizando el modo "r" (read).
# Abrimos el archivo en modo lectura
archivo = open("10_Archivos/prueba.txt", "r")

# Leemos todo el contenido del archivo
texto = archivo.read()

# Cerramos el archivo
archivo.close()

# Imprimimos el contenido del archivo
print(texto)

# Lectura del Archivo como Lista
# ------------------------------
# En lugar de leer todo el contenido como una sola cadena, también podemos leerlo como una lista de líneas utilizando readlines().
# Abrimos el archivo en modo lectura
archivo = open("10_Archivos/prueba.txt", "r")

# Leemos el contenido del archivo y lo convertimos en una lista de líneas
texto = archivo.readlines()

# Cerramos el archivo
archivo.close()

# Imprimimos la lista de líneas
print(texto)

# Usar with y seek para Leer Archivos
# -----------------------------------
# La sentencia with es muy útil porque cierra automáticamente el archivo cuando se sale del bloque with, incluso si ocurre una excepción.
with open("10_Archivos/prueba.txt", "r") as archivo:  # Abrimos el archivo en modo lectura
    # Leemos el contenido del archivo por líneas y lo imprimimos
    print(archivo.readlines())

    # Mover el cursor al inicio del archivo utilizando seek(0)
    archivo.seek(0)

    # Leemos e imprimimos cada línea del archivo
    for linea in archivo:
        print(linea)

# Agregar Contenido a un Archivo
# ------------------------------
# Podemos agregar contenido a un archivo sin borrar el contenido existente utilizando el modo "a+" (append y read).
# Abrimos el archivo en modo agregar y lectura
archivo = open("10_Archivos/prueba.txt", "a+")

# Agregamos una línea al final del archivo
archivo.write("\nFin del archivo")

# Cerramos el archivo
archivo.close()

# Lectura y Escritura Simultáneas
# -------------------------------
# En este ejemplo, abrimos el archivo en modo "r+" (read y write) para leer y escribir simultáneamente.
# Abrimos el archivo en modo lectura y escritura
with open("10_Archivos/prueba.txt", "r+") as archivo:
    # Leemos el contenido del archivo como una lista de líneas
    texto = archivo.readlines()

    # Mover el cursor al inicio del archivo utilizando seek(0)
    archivo.seek(0)

    # Modificamos la primera línea de la lista
    texto[0] = "Esta es una nueva línea\n"

    # Escribimos las líneas modificadas de vuelta en el archivo
    archivo.writelines(texto)
