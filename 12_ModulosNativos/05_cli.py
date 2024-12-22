"""
Módulo CLI para renombrar archivos o directorios

Este script proporciona una interfaz de línea de comandos (CLI) para renombrar
archivos o directorios. Utiliza los módulos 'sys', 'pathlib' y 'os' para manejar
argumentos de línea de comandos, rutas de archivos y operaciones del sistema operativo.

Uso:
    python 12_ModulosNativos/05_cli.py <nombre_original> <nuevo_nombre>

Ejemplo:
    python 12_ModulosNativos/05_cli.py 12_ModulosNativos/prueba 12_ModulosNativos/prueba.md

Autor: Francisco Pérez
Fecha: 23-Agosto-2024
"""

import sys
from pathlib import Path
import os


def cli(args):
    """
    Función principal que maneja la lógica de renombrar archivos o directorios.

    Args:
        args (list): Lista de argumentos de línea de comandos.
              args[0] es el nombre del script,
              args[1] es el nombre original del archivo/directorio,
              args[2] es el nuevo nombre del archivo/directorio.

    Returns:
        None
    """
    print(f"Argumentos recibidos: {args}")

    # Verificar si se proporcionaron argumentos
    if len(args) == 1:
        print("No se ha especificado ningún argumento.")
        return

    # Verificar si se proporcionaron exactamente 2 argumentos (además del nombre del script)
    if len(args) != 3:
        print("Se necesitan 2 argumentos: nombre original y nuevo nombre.")
        return

    # Obtener y verificar el archivo/directorio de origen
    origen = args[1]
    o = Path(origen)
    print(f"Archivo de origen: {o}")
    print(f"¿El archivo de origen existe? {o.exists()}")

    if not o.exists():
        print("El archivo o directorio especificado no existe.")
        return

    # Obtener y verificar el archivo/directorio de destino
    destino = args[2]
    d = Path(destino)
    print(f"Archivo de destino: {d}")
    print(f"¿El archivo de destino existe? {d.exists()}")

    if d.exists():
        print("El archivo o directorio de destino ya existe.")
        return

    # Intentar renombrar el archivo/directorio
    try:
        os.rename(o, d)
        print(f"El archivo o directorio '{
              origen}' ha sido renombrado a '{destino}'.")
    except Exception as e:
        print(f"Error al renombrar el archivo: {e}")


if __name__ == "__main__":
    # Ejecutar la función cli con los argumentos de línea de comandos
    cli(sys.argv)

# para el ejemplo creo un archivo prueba y lo renombro así: python 12_ModulosNativos/05_cli.py 12_ModulosNativos/prueba 12_ModulosNativos/prueba.md
"""
Notas adicionales para estudiantes:

Se usa Ctrl + C para detener la ejecución de un script en la terminal. 
Ctrl + . para instalar el paquete de Python en caso de que no esté instalado.

1. sys.argv: Es una lista en Python que contiene los argumentos de línea de comandos 
   pasados al script. sys.argv[0] es siempre el nombre del script.

2. pathlib.Path: Es una clase que proporciona una interfaz orientada a objetos 
   para trabajar con rutas de archivos y directorios.

3. os.rename(): Es una función que permite renombrar archivos o directorios.

4. Manejo de excepciones: Utilizamos un bloque try-except para manejar posibles 
   errores durante el proceso de renombrado.

5. if __name__ == "__main__": Esta condición asegura que el código dentro de 
   ella solo se ejecute si el script se está ejecutando directamente y no si 
   se está importando como un módulo.

Ejercicios para estudiantes:
1. Modifica el script para que también pueda mover archivos a diferentes directorios.
2. Añade una opción para renombrar múltiples archivos a la vez.
3. Implementa una confirmación antes de renombrar para evitar cambios accidentales.
"""
