# # Comprimidos

# Importamos la clase Path del módulo pathlib para manejar rutas de archivos
from pathlib import Path
# Importamos la clase ZipFile del módulo zipfile para trabajar con archivos comprimidos ZIP
from zipfile import ZipFile

# # Creamos un archivo ZIP llamado "datos.zip" en modo escritura
# with ZipFile("10_Archivos/datos.zip", "w") as archivo_zip:
#     # Recorremos todos los archivos en el directorio "10_Archivos" excepto "datos.zip" para que no se comprima a sí mismo
#     for path in Path().rglob("*.*"):
#         # print(path)  # vemos que archivos se van a comprimir icluido el archivo "datos.zip"
#         if str(path) != "10_Archivos/datos.zip":
#             archivo_zip.write(path)  # Agregamos cada archivo al archivo ZIP

# # Leer un archivo ZIP

# with ZipFile("10_Archivos/datos.zip", "r") as archivo_zip:
#     # Mostramos los nombres de los archivos en el archivo ZIP
#     print(archivo_zip.namelist())


# # Importamos la clase Path del módulo pathlib para manejar rutas de archivos
# from pathlib import Path
# # Importamos la clase ZipFile del módulo zipfile para trabajar con archivos comprimidos ZIP
# from zipfile import ZipFile

# # Lista de archivos que quieres incluir en el ZIP
# archivos_a_incluir = [
#     "10_Archivos/04_csv.py",
#     "10_Archivos/datos.json",
#     "10_Archivos/03_open.py"
#     # Agrega aquí más rutas de archivos que quieras incluir
# ]

# # Creamos un archivo ZIP llamado "datos.zip" en modo escritura
# with ZipFile("10_Archivos/datos.zip", "w") as archivo_zip:
#     for ruta_archivo in archivos_a_incluir:
#         path = Path(ruta_archivo)
#         if path.exists() and path.is_file():
#             archivo_zip.write(path, path.relative_to(Path("10_Archivos")))
#             print(f"Agregado: {path}")
#         else:
#             print(f"No se pudo agregar: {path} (no existe o no es un archivo)")

# # Leer un archivo ZIP
# with ZipFile("10_Archivos/datos.zip", "r") as archivo_zip:
#     # Mostramos los nombres de los archivos en el archivo ZIP
#     print("\nContenido del archivo ZIP:")
#     print(archivo_zip.namelist())


# # Información de un archivo específico en el ZIP

# with ZipFile("10_Archivos/datos.zip", "r") as archivo_zip:
#     info_archivo = archivo_zip.getinfo("04_csv.py")
#     print("\nInformación del archivo 04_csv.py:")
#     print(f"Nombre: {info_archivo.filename}")
#     print(f"Tamaño original: {info_archivo.file_size} bytes")
#     print(f"Tamaño comprimido: {info_archivo.compress_size} bytes")
#     print(f"Porcentaje de compresión: {
#         info_archivo.compress_size / info_archivo.file_size * 100:.2f}%")

# # extraer un archivo del ZIP

# with ZipFile("10_Archivos/datos.zip", "r") as archivo_zip:
#     archivo_zip.extract("04_csv.py", "10_Archivos/extraidos")
#     print("\nArchivo extraído con éxito")

# extraer todos los archivos del ZIP

with ZipFile("10_Archivos/datos.zip", "r") as archivo_zip:
    archivo_zip.extractall("10_Archivos/extraidos")
    print("\nArchivos extraídos con éxito")
