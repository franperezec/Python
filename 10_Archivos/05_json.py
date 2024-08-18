# Archivos JSON en Python
# =======================
# JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y fácil de leer.
# Aunque originalmente derivado de JavaScript, JSON se ha convertido en un formato independiente del lenguaje.
# Es ampliamente utilizado para almacenar y transportar datos entre un servidor y una aplicación web, o entre diferentes sistemas.

import json  # Importamos el módulo json para trabajar con archivos JSON
# Importamos la clase Path del módulo pathlib para manejar rutas de archivos
from pathlib import Path

# Crear un Objeto Path para un Archivo JSON
# -----------------------------------------
# Aquí definimos un objeto Path que representa la ubicación del archivo "datos.json" en el directorio "10_Archivos".
# Este archivo será utilizado para almacenar los datos en formato JSON.

# Ejemplo de datos: una lista de diccionarios que representa clientes
clientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Pallares",
        "edad": 28, "ciudad": "Bogotá"},
    {"id": 2, "nombre": "María", "apellido": "López",
        "edad": 24, "ciudad": "Medellín"},
    {"id": 3, "nombre": "Carlos", "apellido": "González", "edad": 32, "ciudad": "Cali"}
]

# Convertir Datos a Formato JSON
# ------------------------------
# Convertimos la lista de diccionarios "clientes" a una cadena en formato JSON.
# Utilizamos `indent=4` para hacer que el JSON resultante sea más legible con una indentación de 4 espacios.
data = json.dumps(clientes, indent=4)
print(data)  # Imprimimos el JSON generado para verificar su contenido

# Guardar el JSON en un Archivo
# -----------------------------
# Escribimos el JSON generado en un archivo llamado "datos.json" ubicado en "10_Archivos".
# Si el archivo no existe, se crea; si ya existe, se sobrescribe.
Path("10_Archivos/datos.json").write_text(data)

# Leer un Archivo JSON
# --------------------
# Ahora vamos a leer el contenido del archivo "datos.json" para convertirlo de vuelta a una estructura de datos de Python.
# Leemos el contenido del archivo como una cadena de texto
data = Path("10_Archivos/datos.json").read_text(encoding="utf-8")
# Convertimos la cadena JSON a una lista de diccionarios
clientes = json.loads(data)
# Imprimimos la lista de clientes para verificar que se haya leído correctamente
print(clientes)

# Modificar un Archivo JSON
# -------------------------
# Vamos a modificar la estructura de datos que acabamos de leer. En este caso, cambiamos la ciudad del primer cliente.
# Modificamos el valor de la clave "ciudad" en el primer diccionario
clientes[0]["ciudad"] = "Ambato"

# Guardar los Cambios en el Archivo JSON
# --------------------------------------
# Finalmente, guardamos los cambios de vuelta en el archivo "datos.json".
# Convertimos la lista de diccionarios modificada a JSON y sobrescribimos el archivo original.
# Guardamos el JSON con la lista de clientes actualizada
Path("10_Archivos/datos.json").write_text(json.dumps(clientes, indent=4))
