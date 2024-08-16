# Excepciones Personalizadas en Python
# ====================================
#
# En Python, puedes crear tus propias excepciones personalizadas para manejar situaciones específicas
# en tu código. Esto es útil cuando necesitas capturar y manejar errores que no están cubiertos por
# las excepciones integradas de Python. Al definir excepciones personalizadas, puedes proporcionar
# mensajes de error y códigos que sean específicos a la lógica de tu aplicación, lo que facilita la
# identificación y el manejo de problemas en tu código.

# Definición de una Excepción Personalizada
# -----------------------------------------
#
# Para crear una excepción personalizada en Python, defines una nueva clase que herede de la clase base `Exception`.
# Esto te permite crear una excepción que se comporte como cualquier otra excepción de Python, pero con la flexibilidad
# de personalizar su mensaje y agregar atributos adicionales.

class MiError(Exception):
    """
    Esta clase define una excepción personalizada llamada `MiError`. 
    Esta excepción se puede utilizar para representar errores específicos en tu programa.
    """

    def __init__(self, mensaje, codigo):
        """
        El método `__init__` se llama cuando se crea una nueva instancia de la clase `MiError`.
        - `mensaje`: El mensaje de error que describe el problema.
        - `codigo`: Un código de error que puede ser utilizado para identificar el tipo de problema.
        """
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        """
        El método `__str__` convierte el objeto de la excepción en una cadena cuando se requiere.
        Aquí, devuelve el mensaje de error formateado junto con el código de error.
        """
        return f"MiError: {self.mensaje} - código: {self.codigo}"

# Uso de la Excepción Personalizada en Funciones
# ----------------------------------------------
#
# Puedes utilizar tu excepción personalizada en cualquier parte de tu código donde tenga sentido.
# A continuación se muestra cómo podrías utilizar `MiError` en una función simple de división.


def division(n=0):
    if n == 0:
        # Si `n` es cero, lanzamos una excepción personalizada `MiError`.
        # Aquí, se utiliza un mensaje descriptivo y un código de error (por ejemplo, 404)
        # para ayudar a identificar el problema.
        raise MiError("No se puede dividir por cero", 404)
    return 5 / n

# Manejo de la Excepción Personalizada
# ------------------------------------
#
# Como con cualquier otra excepción en Python, puedes capturar tu excepción personalizada
# usando un bloque `try-except`. Esto te permite manejar el error de manera controlada.


try:
    division()  # Intenta ejecutar la función `division` con el valor predeterminado de `n`, que es 0
except MiError as error:
    # Captura la excepción personalizada `MiError`
    # El mensaje y el código de error definidos en la excepción se imprimen aquí.
    print("Ocurrió un error:", error)

# En este ejemplo:
# - La función `division()` lanza la excepción `MiError` si se intenta dividir por cero.
# - El bloque `try-except` captura esta excepción y muestra un mensaje con los detalles del error.
# - Esto permite que el programa maneje el error de manera específica y controlada, en lugar de detenerse abruptamente.

# Conclusión
# ==========
# Las excepciones personalizadas en Python te permiten manejar errores de manera más precisa y específica.
# Puedes proporcionar información adicional sobre los errores, como mensajes personalizados y códigos de error,
# lo que facilita el diagnóstico y la resolución de problemas. Al capturar estas excepciones en tus bloques `try-except`,
# puedes asegurar que tu programa reaccione de manera adecuada a los errores que sean específicos a la lógica de tu aplicación.
