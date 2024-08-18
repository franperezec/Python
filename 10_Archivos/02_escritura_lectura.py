# Escritura y Lectura de Archivos en Python
# =========================================
# En este ejemplo, vamos a explorar cómo leer y escribir en archivos de texto utilizando
# la clase Path del módulo pathlib. Este módulo proporciona una forma moderna y eficiente
# de trabajar con archivos y rutas en Python.

# Importamos el módulo pathlib para trabajar con archivos y rutas
from pathlib import Path

# Crear un Objeto Path para un Archivo Específico
# -----------------------------------------------
# Creamos un objeto Path que representa el archivo "prueba.txt" ubicado en el directorio "10_Archivos".
archivo = Path("10_Archivos/prueba.txt")

# Leer el Contenido del Archivo
# -----------------------------
# Leemos todo el contenido del archivo y lo convertimos en una lista de líneas.
# El archivo se lee utilizando la codificación "utf-8", que es adecuada para el idioma español.
# La función split("\n") divide el contenido en una lista donde cada elemento es una línea del archivo.
texto = archivo.read_text("utf-8").split("\n")

# Imprimimos el contenido del archivo como una lista, donde cada línea es un elemento de la lista.
print(texto)

# Iteramos sobre cada línea de la lista y la imprimimos.
# Esto nos permite ver el contenido del archivo línea por línea.
for linea in texto:
    print(linea)  # Imprime cada línea del archivo

# Modificar el Contenido del Archivo
# ----------------------------------
# Ahora vamos a modificar el contenido del archivo:
# - Insertamos "Hola mundo" al inicio del archivo.
# - Añadimos "Fin del archivo" al final del archivo.

# Insertar "Hola mundo" en la primera posición de la lista (al inicio del archivo)
texto.insert(0, "Hola mundo")

# Añadir "Fin del archivo" en la última posición de la lista (al final del archivo)
texto.append("Fin del archivo")

# Escribir el Contenido Modificado en el Archivo
# ----------------------------------------------
# Convertimos la lista de líneas de nuevo a una única cadena de texto usando "\n".join(texto),
# que une todos los elementos de la lista en una sola cadena, separada por saltos de línea.
# Luego, escribimos esta cadena en el archivo, sobrescribiendo su contenido original.
# También especificamos la codificación "utf-8" para mantener la consistencia en el manejo de caracteres especiales.
archivo.write_text("\n".join(texto), "utf-8")

# Imprimimos un mensaje indicando que el archivo ha sido modificado exitosamente.
print("Archivo modificado")

# Notas Importantes:
# ------------------
# - Este enfoque es adecuado para archivos de texto plano pequeños, donde todo el contenido del archivo
#   puede cargarse en la memoria sin problemas.
# - Para archivos más grandes, es recomendable trabajar con partes del archivo (chunks) en lugar de
#   cargar todo el archivo en la memoria, para evitar problemas de rendimiento y uso excesivo de memoria.
