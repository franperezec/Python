# Inyección de Dependencias en Programación
# =========================================
# La inyección de dependencias es una técnica de programación en la que una clase recibe
# las instancias de los objetos que necesita para funcionar desde el exterior, en lugar de
# crearlos internamente. Esto permite que la clase sea más flexible, fácil de probar y
# más desacoplada de las implementaciones específicas de sus dependencias.

# Ejemplo con Clases
# ==================
# Supongamos que estamos desarrollando una aplicación para gestionar automóviles, y
# necesitamos una clase `Coche` que tenga una relación con una clase `Cinturon`.

# Ejemplo sin Inyección de Dependencias
# -------------------------------------
# En un enfoque tradicional sin inyección de dependencias, la clase `Coche` es responsable
# de crear su propia instancia de `Cinturon`. Esto crea un acoplamiento fuerte entre `Coche`
# y `Cinturon`, lo que dificulta cambiar la implementación de `Cinturon` o realizar pruebas
# unitarias de la clase `Coche`.

# Vamos a crear una librería Cinturon para una clase Coche.
# import Cinturon

# class Coche:
#     def __init__(self):
#         self.cinturon = Cinturon()  # La clase Coche crea su propia instancia de Cinturon

# Ejemplo con Inyección de Dependencias
# -------------------------------------
# En lugar de crear una instancia de `Cinturon` dentro de la clase `Coche`, es mejor inyectar
# la dependencia a través del constructor de `Coche`. De esta manera, podemos pasar cualquier
# objeto que implemente la interfaz o los métodos que `Cinturon` debería tener, lo que hace
# que `Coche` sea más flexible y fácil de probar.

# Es mejor inyectar la dependencia en el constructor

# class Coche:
#     def __init__(self, cinturon):  # Aquí, `cinturon` es inyectado desde fuera
#         self.cinturon = cinturon

# Ejemplo con Funciones
# =====================
# La inyección de dependencias no se limita a clases; también se puede aplicar a funciones.
# Aquí tenemos un ejemplo con una función `guardar()` que depende de una entidad que tiene
# un método `guardar()`.

# Ejemplo sin Inyección de Dependencias
# -------------------------------------
# En un enfoque sin inyección de dependencias, la función `guardar()` depende directamente
# de un módulo específico, en este caso, `usuario`. Esto limita la reutilización de la
# función y la hace dependiente de una implementación específica.

# import usuario

# def guardar():
#     usuario.guardar()  # La función guardar depende directamente de la implementación del módulo usuario

# Ejemplo con Inyección de Dependencias
# -------------------------------------
# Con la inyección de dependencias, la función `guardar()` acepta una entidad externa que
# se inyecta en la función. Esto permite que la función sea más flexible y reusable, ya
# que no está acoplada a un módulo específico.

# def guardar(entidad):  # La entidad es inyectada, lo que permite reutilizar la función con diferentes implementaciones
#     entidad.guardar()

# Ejemplo en Flask
# ================
# La inyección de dependencias es común en frameworks como Flask, donde las dependencias
# se suelen inyectar en las vistas o controladores. Aquí tienes un ejemplo simple donde
# se inyecta una aplicación Flask en una función.

# from flask import Flask  # Flask inyecta la aplicación en el contexto de la función, lo que permite su configuración

# La inyección de dependencias permite:
# - **Código Reutilizable**: Puedes reutilizar la clase o función con diferentes implementaciones de sus dependencias.
# - **Código Más Limpio y Mantenible**: El código es más modular, lo que facilita su mantenimiento.
# - **Facilidad de Pruebas**: Puedes inyectar dependencias simuladas (mocks) para realizar pruebas unitarias de manera más efectiva.


# ----------------------------------------
# Importación Dinámica de Paquetes en Python
# ==========================================
#
# En este ejemplo, vamos a realizar una importación dinámica de módulos desde dos directorios
# específicos. El objetivo es cargar estos módulos en tiempo de ejecución y ejecutar sus
# respectivas funciones `init()` con dependencias inyectadas.
#
# Esto es útil en aplicaciones modulares o sistemas de plugins donde los módulos pueden ser
# cargados o actualizados sin necesidad de modificar el código base.

# Importamos la clase Path para trabajar con rutas de archivos y directorios
from pathlib import Path
import importlib  # Importamos importlib para realizar importaciones dinámicas de módulos
import sys  # Importamos sys para manipular la ruta de búsqueda de módulos en tiempo de ejecución

# Ruta Absoluta del Directorio Actual
# -----------------------------------
# Obtenemos la ruta absoluta del directorio donde se encuentra el script que se está ejecutando.
# Esto nos permite trabajar con rutas absolutas, lo que es más seguro y confiable.
current_dir = Path(__file__).parent.absolute()

# Añadir el Directorio Actual a sys.path
# --------------------------------------
# sys.path es una lista de rutas donde Python busca los módulos cuando se realiza una importación.
# Al añadir el directorio actual a sys.path, aseguramos que Python pueda encontrar e importar
# los módulos que queremos cargar dinámicamente.
sys.path.append(str(current_dir))

# Obtener Solo los Directorios
# ----------------------------
# Usamos Path.iterdir() para obtener todos los elementos dentro del directorio actual.
# Luego filtramos para quedarnos solo con los directorios. Esto es porque asumimos que cada
# directorio representa un módulo independiente que queremos cargar.
paths = [p for p in current_dir.iterdir() if p.is_dir()]

# Definir las Dependencias
# ------------------------
# Creamos un diccionario con las dependencias que serán inyectadas en los módulos cargados.
# Aquí se asume que cada módulo tiene una función init() que acepta estas dependencias como parámetros.
dependencies = {
    "db": "base de datos",  # Esta cadena representa una referencia ficticia a un objeto `db`
    "api": "api",  # Esta cadena representa una referencia ficticia a un objeto `api`
    # Esta cadena representa una referencia ficticia a un objeto `graphql`
    "graphql": "graphql",
    "utils": "utilidades"  # Esta cadena representa una referencia ficticia a un objeto `utils`
}

# Función para Cargar Módulos
# ---------------------------
# Esta función se encarga de cargar dinámicamente cada módulo basado en el nombre del directorio.
# Después de la importación, verifica si el módulo tiene una función init() y si es ejecutable (callable).
# Si es así, la función init() es llamada con las dependencias inyectadas.


def load(p):
    # Construir el nombre del módulo
    # ------------------------------
    # El nombre del módulo se construye basado en el nombre del directorio.
    module_name = p.name
    try:
        # Importar el Módulo Dinámicamente
        # --------------------------------
        # Usamos importlib para importar el módulo de manera dinámica.
        module = importlib.import_module(module_name)

        # Verificar si el Módulo tiene una Función init()
        # ----------------------------------------------
        # Usamos hasattr() para comprobar si el módulo tiene una función llamada init().
        # Luego verificamos si esa función es callable, es decir, si puede ser ejecutada.
        if hasattr(module, 'init') and callable(module.init):
            # Llamar a la Función init() con las Dependencias Inyectadas
            # ---------------------------------------------------------
            # Si la función init() existe y es callable, la llamamos con las dependencias.
            module.init(**dependencies)
        else:
            print(f"El módulo {
                  module_name} no tiene una función init() ejecutable.")
    except ImportError as e:
        # Manejar Errores de Importación
        # ------------------------------
        # Si ocurre un error durante la importación del módulo, lo capturamos e imprimimos un mensaje de error.
        print(f"No se pudo importar el módulo {module_name}: {e}")


# Ejecutar la Función load para Cada Directorio
# --------------------------------------------
# Usamos map() para aplicar la función load() a cada directorio en la lista paths.
# Esto permite cargar y ejecutar dinámicamente todos los módulos en los subdirectorios del directorio actual.
list(map(load, paths))
