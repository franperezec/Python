# Else y Finally en el Manejo de Excepciones
# ==========================================
# En Python, las excepciones se manejan comúnmente utilizando bloques `try` y `except`. Sin embargo,
# Python ofrece dos herramientas adicionales para el manejo de excepciones: las cláusulas `else` y `finally`.
# Estas cláusulas permiten que tu código sea más claro y expresivo, brindando un control más preciso sobre
# cómo y cuándo se ejecuta el código, especialmente en presencia de errores.

# La Cláusula `else`
# ==================
# La cláusula `else` se ejecuta únicamente si no se produce ninguna excepción en el bloque `try`.
# Es útil cuando tienes código que solo debe ejecutarse si todo lo que está dentro del `try` se ejecuta correctamente.
# De esta manera, puedes separar claramente el manejo de excepciones del código que se ejecuta cuando no hay errores.

# Ejemplo de uso de `else`:

try:
    # Intentamos convertir la entrada en un número
    numero = int(input("Introduce un número: "))
except Exception as error:
    # Este bloque captura cualquier excepción que ocurra en el bloque `try`
    print("Ocurrió un error:", error)
else:
    # Este bloque se ejecuta solo si no se produjo ninguna excepción en el bloque `try`
    print("El código se ejecutó sin errores. El número ingresado es:", numero)

# En este ejemplo:
# - Si el usuario ingresa un valor que no puede ser convertido a un número, se lanza una excepción,
#   y el código dentro del bloque `except` se ejecuta.
# - Si el usuario ingresa un número válido, no se lanza ninguna excepción, y el bloque `else` se ejecuta,
#   mostrando el número ingresado.

# La Cláusula `finally`
# =====================
# La cláusula `finally` se ejecuta siempre, independientemente de si se produjo una excepción o no.
# Esto es particularmente útil para liberar recursos o realizar tareas de limpieza, como cerrar archivos
# o conexiones a bases de datos, que deben ejecutarse sin importar si el código dentro del `try` tuvo éxito o no.

# Ejemplo de uso de `finally`:

try:
    # Intentamos convertir la entrada en un número
    numero = int(input("Introduce un número: "))
except Exception as error:
    # Este bloque captura cualquier excepción que ocurra en el bloque `try`
    print("Ocurrió un error:", error)
finally:
    # Este bloque se ejecuta siempre, independientemente de lo que ocurra en el bloque `try`
    print("El programa ha finalizado")

# En este ejemplo:
# - Si el usuario ingresa un valor que no puede ser convertido a un número, el bloque `except` se ejecuta,
#   seguido del bloque `finally`.
# - Si el usuario ingresa un número válido, el código se ejecuta con éxito, y luego se ejecuta el bloque `finally`.

# Uso Combinado de `else` y `finally`
# ===================================
# Puedes utilizar `else` y `finally` juntos en un bloque de manejo de excepciones. Esto te permite manejar
# todas las posibles situaciones: capturar y manejar excepciones, ejecutar código si no hay errores, y siempre
# realizar una acción final sin importar lo que ocurra.

# Ejemplo completo de uso de `else` y `finally`:

try:
    numero = int(input("Introduce un número: "))
except ValueError as error:
    # Captura un error específico, en este caso un ValueError
    print("Ingrese un valor que corresponda. Ha ocurrido un error de tipo:", error)
else:
    # Se ejecuta solo si no hay excepciones
    print("El número ingresado es:", numero)
finally:
    # Se ejecuta siempre, independientemente de si hubo o no una excepción
    print("El programa ha finalizado")

# En este ejemplo:
# - Si ocurre un `ValueError` (por ejemplo, si el usuario ingresa texto en lugar de un número),
#   se ejecuta el bloque `except` seguido del bloque `finally`.
# - Si no ocurre ninguna excepción, se ejecuta el bloque `else` seguido del bloque `finally`.

# Conclusión
# ==========
# Las cláusulas `else` y `finally` son herramientas poderosas en Python que te permiten controlar con precisión
# el flujo de tu programa en presencia de excepciones. El uso de `else` te permite separar el código que solo debe
# ejecutarse en ausencia de errores, mientras que `finally` asegura que cierto código se ejecute siempre, sin importar
# lo que ocurra. Utilizar estas herramientas de manera adecuada puede mejorar la claridad y robustez de tu código.
