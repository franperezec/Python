# Invocar una Excepción en Python
# ===============================
#
# En Python, es posible invocar una excepción manualmente usando la instrucción `raise`.
# Esta técnica es útil en situaciones donde necesitas forzar un error para probar cómo tu programa maneja
# una excepción específica, o cuando encuentras una condición en tu código que debería generar un error.
#
# La sintaxis básica para invocar una excepción es la siguiente:
#
# raise TipoDeExcepción("Mensaje de error")
#
# Donde `TipoDeExcepción` es el tipo de excepción que deseas invocar, y `"Mensaje de error"` es un mensaje opcional
# que describe el motivo de la excepción. Esta capacidad te permite personalizar los mensajes de error y asegurar
# que las excepciones sean lanzadas en situaciones que lo ameriten.

# Ejemplo: Invocar una Excepción Manualmente
# ==========================================

# Considera la siguiente función `division`, que intenta dividir un número entre otro.
# Normalmente, dividir por cero en Python genera una excepción de tipo `ZeroDivisionError`.
# Sin embargo, en este ejemplo, utilizaremos `raise` para invocar esta excepción manualmente si el divisor es cero.

def division(n=0):
    if n == 0:
        # Si n es cero, se lanza manualmente una excepción de tipo ZeroDivisionError.
        # Esto se hace para asegurarse de que la división por cero sea tratada como un error.
        # Puedes consultar la clasificación completa de excepciones en https://docs.python.org/3/library/exceptions.html
        raise ZeroDivisionError(
            "No se puede dividir por cero", f"El valor de n es {n}")
    return 5 / n

# En este caso, la función `division` comprobará si el valor de `n` es cero. Si lo es, lanzará una excepción
# `ZeroDivisionError` con un mensaje personalizado. De lo contrario, procederá a realizar la división.


# Manejo de la Excepción
# ======================
try:
    division()  # Intenta ejecutar la función `division` con el valor predeterminado de `n`, que es 0
except ZeroDivisionError as error:
    # Si se lanza una excepción, este bloque `except` la captura.
    # El mensaje de error definido en la función `division` será impreso aquí.
    print("Ocurrió un error:", error)

# En el bloque `try`, se llama a la función `division()` con su valor predeterminado (que es cero). Esto provoca que
# se lance una `ZeroDivisionError`. El bloque `except` captura la excepción y muestra el mensaje de error definido
# en la función.

# Información adicional
# =====================
# Para más información sobre excepciones en Python, puedes consultar la documentación oficial:
# https://docs.python.org/3/tutorial/errors.html
# También puedes explorar las excepciones integradas en Python en:
# https://docs.python.org/3/library/exceptions.html
#
# Es importante tener en cuenta que no se debe lanzar una excepción sin una razón justificada.
# Siempre que sea posible, es mejor manejar los errores de manera controlada sin necesidad de lanzar excepciones
# manualmente. Además, las excepciones son costosas en términos de rendimiento, por lo que no deberían usarse
# para controlar el flujo normal de un programa.
