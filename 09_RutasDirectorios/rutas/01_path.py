# Rutas y directorios

from pathlib import Path  # Importamos la clase Path de la librería pathlib

# nos sirve para crear rutas y directorios dentro de nuestro sistema de archivos

# r raw string para que no tome los backslash como caracteres de escape nos  ayuda a que no se interpreten los caracteres especiales
Path(r"C:\Archivos de Programa\Minecraft")  # ruta absoluta en windows
# Pero se debe aprender a hacerlo como en Linus porque las aplicaciones no son solo para windows y se corren en servidores linux
# aprender rutas en Linux para desplegar aplicaciones en servidores

# en Mac o Linux es la siguiente ruta

# Path("/usr/bin") # ruta absoluta en Mac o Linux

# Path() # ruta relativa en donde se encuentra el archivo que se está ejecutando en este caso 01_path.py

# Path("01_path.py") # ruta relativa en donde se encuentra el archivo que se está ejecutando en este caso 01_path.py

# Path.home() # ruta relativa en donde se encuentra el archivo que se está ejecutando en este caso 01_path.py

# ruta relativa en donde se encuentra el archivo que se está ejecutando en este caso 01_path.py
path = Path("rutas/01_path.py")
# también no puede existir el archivo y se crea

path.is_file()  # True si es un archivo

path.is_dir()  # False si es un directorio

path.exists()  # True si existe

print(path.name)  # 01_path.py nombre del archivo
print(path.stem)  # 01_path nombre del archivo sin extensión
print(path.suffix)  # .py extensión del archivo

print(path.parent)  # rutas directorio padre

print(path.absolute())  # ruta absoluta del archivo

p = path.with_name("prueba.py")  # cambia el nombre del archivo
print(p)  # rutas/prueba.py
p = path.with_suffix(".txt")  # cambia la extensión del archivo
print(p)  # rutas/01_path.txt
p = path.with_stem("confianza")  # cambia el nombre del archivo sin extensión
print(p)  # rutas/confianza.py
