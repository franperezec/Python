# Directorios en Python

# Para trabajar con directorios en Python, podemos utilizar la clase Path de la librería pathlib. Con esta clase podemos crear, eliminar y mover directorios, así como listar los archivos que contienen.

# Crear directorios

from pathlib import Path  # Importamos la clase Path de la librería pathlib


# path = Path("nuevo_directorio") # Creamos un objeto Path con el nombre del directorio

# path.mkdir() # Creamos el directorio
# path.rmdir() # Eliminamos el directorio
# path.exists() # Verificamos si el directorio existe
# path.rename("otro_directorio") # Renombramos el directorio

# Creamos un objeto Path con el nombre del directorio
path = Path("09_RutasDirectorios/rutas")

# print(path.iterdir())  # Objeto generador con los archivos del directorio
# <generator object Path.iterdir at 0x00000295131F3780>
# Listamos los archivos del directorio

# usamos un for para recorrer el objeto generador

for archivo in path.iterdir():
    print(archivo)  # Imprimimos el nombre de cada archivo

# transformamos el objeto generador en una lista

# print(list(path.iterdir()))  # Lista con los archivos del directorio
# con for

# Lista con los archivos del directorio
archivos = [p for p in path.iterdir() if not p.is_dir()]
# print(archivos)
# [WindowsPath('09_RutasDirectorios/rutas/01_path.py'), WindowsPath('09_RutasDirectorios/rutas/02_directorios.py')]
# en Windows nos sale WindowsPath en Linux o Mac sería PosixPath

# seleccionar archivos que cumplan con una condición
# Seleccionamos los archivos con extensión .py
archivos = [p for p in path.glob("*.py")]
# [WindowsPath('09_RutasDirectorios/rutas/01_path.py'), WindowsPath('09_RutasDirectorios/rutas/02_directorios.py')]

# seleccionamos los que empiecen con 01
archivos = [p for p in path.glob("01*")]

# [WindowsPath('09_RutasDirectorios/rutas/01_path.py')]

# seleccionamos todas las carpetas **/* para que busque en todas las carpetas
archivos = [p for p in path.glob("**/*.py")]
# es lo mismo que la línea anterior r es recursivo
archivos = [p for p in path.rglob("*.py")]

print(archivos)  # Lista con los archivos seleccionados


# En la terminal de comandos se pueden realizar las siguientes operaciones:
# con cd.. se sube un nivel en la jerarquía de directorios
# con cd nombre_directorio se baja un nivel en la jerarquía de directorios
# con ls se listan los archivos del directorio
# con mkdir nombre_directorio se crea un directorio
# con touch nombre_archivo se crea un archivo
# con rm nombre_archivo se elimina un archivo
# con rm -r nombre_directorio se elimina un directorio
# con mv nombre_archivo nuevo_nombre_archivo se renombra un archivo
# con mv nombre_directorio nuevo_nombre_directorio se renombra un directorio
# con cp nombre_archivo nombre_directorio se copia un archivo a un directorio
# con cp -r nombre_directorio nombre_directorio se copia un directorio a otro directorio
# con cat nombre_archivo se muestra el contenido de un archivo
# con nano nombre_archivo se edita un archivo
