# Gestión de Archivos en Python
# =============================
# En este código, vamos a explorar cómo trabajar con archivos en Python utilizando la clase Path del módulo pathlib.
# También utilizaremos el módulo time para convertir timestamps en fechas legibles.

from pathlib import Path  # Módulo pathlib para trabajar con rutas y archivos
# Módulo time para trabajar con fechas legibles a partir de timestamps
from time import ctime

# Crear un Objeto Path para un Archivo Específico
# -----------------------------------------------
# Creamos un objeto Path que representa el archivo "prueba.txt" en el directorio "10_Archivos".
# Este archivo puede contener cualquier tipo de contenido; en este caso, imaginemos que contiene texto generado
# utilizando un generador de texto como https://www.lipsum.com/.
archivo = Path("10_Archivos/prueba.txt")

# Operaciones Básicas con Archivos
# --------------------------------
# A continuación, se muestran algunas operaciones básicas que se pueden realizar con archivos usando pathlib.

# Verificar si el archivo existe
# archivo.exists()  # Retorna True si el archivo existe

# Renombrar el archivo
# archivo.rename("10_Archivos/nuevo_nombre.txt")  # Cambia el nombre del archivo

# Eliminar el archivo
# archivo.unlink()  # Elimina el archivo del sistema de archivos

# Obtener Información del Archivo
# -------------------------------
# Podemos obtener información detallada del archivo usando el método stat().
# Este método devuelve un objeto con varios atributos que describen el archivo.

# print(archivo.stat())  # Imprime información detallada del archivo

# La salida de archivo.stat() incluye los siguientes atributos:
# st_mode: Tipo de archivo y permisos
# st_ino: Número de inodo (identificador único en el sistema de archivos)
# st_dev: Número de dispositivo (identificador del dispositivo de almacenamiento)
# st_nlink: Número de enlaces (número de nombres que apuntan al archivo)
# st_uid: Identificador de usuario del propietario del archivo
# st_gid: Identificador de grupo del propietario del archivo
# st_size: Tamaño del archivo en bytes
# st_atime: Tiempo de último acceso al archivo (en formato timestamp)
# st_mtime: Tiempo de última modificación del archivo (en formato timestamp)
# st_ctime: Tiempo de creación del archivo (en formato timestamp, en algunos sistemas puede ser la última modificación del metadato)

# Convertir Timestamps a Fechas Legibles
# --------------------------------------
# Los tiempos de acceso, modificación y creación se almacenan como timestamps (segundos desde el 1 de enero de 1970).
# Podemos convertir estos valores en un formato de fecha legible usando la función ctime().

# Tiempo de último acceso al archivo en formato legible
# Ejemplo de salida: Sat Aug 17 21:58:29 2024
print("acceso: ", ctime(archivo.stat().st_atime))

# Tiempo de creación del archivo en formato legible
# Ejemplo de salida: Sat Aug 17 21:57:01 2024
print("creación: ", ctime(archivo.stat().st_ctime))

# Tiempo de última modificación del archivo en formato legible
# Ejemplo de salida: Sat Aug 17 21:58:29 2024
print("modificación: ", ctime(archivo.stat().st_mtime))

"""
El resultado de estas operaciones podría ser algo como:

acceso:  Sat Aug 17 21:58:29 2024
creación:  Sat Aug 17 21:57:01 2024
modificación:  Sat Aug 17 21:58:29 2024

Esto indica cuándo fue la última vez que el archivo fue accedido, creado y modificado, en un formato de fecha legible para humanos.
"""
