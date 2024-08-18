# Archivos CSV en Python
# ======================
# Los archivos CSV (Comma-Separated Values) son un formato común para almacenar datos tabulares.
# Son ampliamente utilizados en hojas de cálculo, bases de datos y otros conjuntos de datos.
# En un archivo CSV, cada línea representa una fila de datos, y los valores en cada fila están separados por comas (u otro delimitador).

# Python proporciona varias formas de trabajar con archivos CSV, incluyendo el módulo csv estándar
# y bibliotecas de terceros como pandas. En este ejemplo, exploraremos cómo leer y escribir archivos CSV
# utilizando el módulo csv de Python.

import csv  # Importamos el módulo csv para trabajar con archivos CSV
import os  # Importamos el módulo os para manipular archivos, como eliminar y renombrar
import shutil  # Importamos el módulo shutil para copiar y mover archivos

# Escribir Datos en un Archivo CSV
# --------------------------------
# Vamos a escribir datos en un archivo CSV utilizando el módulo csv.

# with open("10_Archivos/datos.csv", "w", newline="") as archivo_csv:
#     # Abrimos el archivo "datos.csv" en modo escritura ("w").
#     # El parámetro newline="" asegura que no se añadan líneas en blanco adicionales en algunos sistemas.
#
#     # Creamos un objeto escritor que nos permitirá escribir en el archivo CSV
#     escritor = csv.writer(archivo_csv)
#
#     # Escribimos una fila de encabezado con los nombres de las columnas
#     escritor.writerow(["Nombre", "Edad", "Género"])
#
#     # Escribimos filas de datos con la información de cada persona
#     escritor.writerow(["Juan", 28, "Masculino"])
#     escritor.writerow(["María", 24, "Femenino"])
#     escritor.writerow(["Carlos", 32, "Masculino"])
#
# # Imprimimos un mensaje indicando que los datos han sido escritos en el archivo CSV
# print("Datos escritos en el archivo CSV")

# Leer Datos de un Archivo CSV
# ----------------------------
# Ahora, vamos a leer los datos del archivo CSV que acabamos de crear.

# with open("10_Archivos/datos.csv", "r", newline="") as archivo_csv:
#     # Abrimos el archivo "datos.csv" en modo lectura ("r").
#     # El parámetro newline="" asegura que las líneas se lean correctamente.
#
#     # Creamos un objeto lector que nos permitirá leer el archivo CSV
#     lector = csv.reader(archivo_csv)
#
#     # Convertimos todo el contenido del archivo en una lista y lo imprimimos
#     print(list(lector))
#
#     # Movemos el cursor al inicio del archivo para poder volver a leerlo
#     archivo_csv.seek(0)
#
#     # Iteramos sobre cada fila del archivo CSV e imprimimos los datos
#     for fila in lector:
#         print(fila)

# Actualización de Datos en un Archivo CSV
# ----------------------------------------
# Ahora, vamos a actualizar los datos del archivo CSV. En este ejemplo, modificaremos la edad de "Carlos" de 32 a 40.

# Ruta de los archivos
datos_csv = "10_Archivos/datos.csv"  # Ruta del archivo CSV original
# Ruta de un archivo temporal donde se almacenarán los datos actualizados
temp_csv = "10_Archivos/temp.csv"

# Leer del archivo original y escribir en el archivo temporal
with open(datos_csv, 'r', newline='') as r, open(temp_csv, 'w', newline='') as w:
    # Abrimos el archivo original en modo lectura y el archivo temporal en modo escritura

    # Creamos un objeto lector para leer el archivo original
    reader = csv.reader(r)
    # Creamos un objeto escritor para escribir en el archivo temporal
    writer = csv.writer(w)

    # Iteramos sobre cada fila del archivo original
    for row in reader:
        # Si encontramos la fila de "Carlos", actualizamos su edad a 40
        if row[0] == "Carlos":
            # Escribimos la fila actualizada en el archivo temporal
            writer.writerow(["Carlos", "40", "Masculino"])
        else:
            # Escribimos las otras filas sin cambios en el archivo temporal
            writer.writerow(row)

# Reemplazar el archivo original con el archivo temporal
try:
    os.remove(datos_csv)  # Eliminamos el archivo original
    # Renombramos el archivo temporal para que reemplace al original
    os.rename(temp_csv, datos_csv)
except PermissionError:
    print("No se pudo acceder al archivo. Asegúrate de que no esté abierto en otra aplicación.")
    # Si no podemos eliminar o renombrar el archivo, intentamos copiar el contenido del archivo temporal al original
    try:
        # Copiamos el archivo temporal sobre el original
        shutil.copy2(temp_csv, datos_csv)
        # Eliminamos el archivo temporal después de la copia
        os.remove(temp_csv)
    except Exception as e:
        # Informamos si ocurre algún error durante el proceso
        print(f"Error al reemplazar el archivo: {e}")
