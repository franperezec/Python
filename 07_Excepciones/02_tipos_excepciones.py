# Introducción a las Excepciones en Python
# ========================================

# Las excepciones en Python son mecanismos que nos permiten manejar errores de manera controlada.
# En lugar de que un error detenga la ejecución de todo el programa, las excepciones permiten capturar
# esos errores, manejar la situación de manera adecuada, y continuar con la ejecución o terminar el programa
# de forma ordenada.

# Excepciones Comunes en Python
# =============================
# Aquí te presentamos algunas de las excepciones más comunes que encontrarás al programar en Python:

# 1. **ZeroDivisionError**: Ocurre cuando intentas dividir un número por cero.
# 2. **NameError**: Aparece cuando intentas acceder a una variable que no ha sido definida.
# 3. **TypeError**: Se produce cuando intentas realizar una operación con tipos de datos que no son compatibles.
# 4. **ValueError**: Ocurre cuando intentas realizar una operación con un valor que no es adecuado.
# 5. **IndexError**: Sucede cuando intentas acceder a un índice que no existe en una lista o tupla.
# 6. **KeyError**: Aparece cuando intentas acceder a una clave que no existe en un diccionario.
# 7. **FileNotFoundError**: Se produce cuando intentas abrir un archivo que no existe.
# 8. **IOError**: Ocurre durante operaciones de entrada/salida, como al leer o escribir en un archivo.
# 9. **ImportError**: Aparece cuando intentas importar un módulo que no se encuentra disponible.
# 10. **KeyboardInterrupt**: Se genera cuando se interrumpe la ejecución de un programa con Ctrl+C.
# 11. **AttributeError**: Ocurre cuando intentas acceder a un atributo que no existe en un objeto.

# Recuerda que puedes consultar la lista completa de excepciones en la documentación oficial de Python.

# Manejo de Excepciones en Python
# ===============================
# Para manejar las excepciones en Python y evitar que el programa se detenga de manera inesperada,
# utilizamos la estructura `try-except`. Esta estructura nos permite capturar y manejar excepciones
# de manera controlada.

# Estructura Básica de try-except
# -------------------------------
# La estructura `try-except` se compone de dos bloques de código:
# 1. El bloque `try` contiene el código que puede generar una excepción.
# 2. El bloque `except` contiene el código que se ejecuta si ocurre una excepción durante la ejecución del bloque `try`.

# La sintaxis básica es la siguiente:

# try:
#     # Código que puede arrojar una excepción
# except TipoDeExcepción as variable:
#     # Código que se ejecuta en caso de que se produzca una excepción

# Donde `TipoDeExcepción` es la excepción específica que deseas capturar, y `variable` es un nombre que puedes usar para
# almacenar el objeto de la excepción y acceder a más detalles sobre ella.

# Ejemplo: Manejo de ZeroDivisionError
# ------------------------------------
try:
    resultado = 10 / 0  # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError as error:
    print("Error:", error)

# En este ejemplo, intentamos dividir 10 por 0, lo cual genera una excepción de tipo `ZeroDivisionError`.
# El bloque `except` captura esa excepción y muestra un mensaje de error en la consola.

# Captura Genérica de Excepciones
# -------------------------------
# También es posible capturar cualquier tipo de excepción sin especificar cuál es. Esto se hace omitiendo el tipo de excepción:

try:
    resultado = 10 / 0  # Genera una excepción
except:
    print("Se ha producido un error")

# En este caso, el bloque `except` captura cualquier excepción que ocurra dentro del bloque `try`. Si ejecutas este código,
# verás el mensaje "Se ha producido un error" en la consola.

# Aunque esto es útil en algunos casos, generalmente es mejor capturar excepciones específicas para evitar ocultar errores
# inesperados.

# Estructura try-except-finally
# -----------------------------
# La estructura `try-except-finally` permite ejecutar un bloque de código adicional después de que se ha producido una excepción,
# independientemente de si la excepción fue capturada o no.

# try:
#     # Código que puede arrojar una excepción
# except TipoDeExcepción as variable:
#     # Código que se ejecuta en caso de que se produzca una excepción
# finally:
#     # Código que se ejecuta después de que se haya producido una excepción

# Ejemplo de try-except-finally:
try:
    resultado = 10 / 0  # Genera una excepción ZeroDivisionError
except ZeroDivisionError as error:
    print("Error:", error)
finally:
    print("El programa ha finalizado")

# En este ejemplo, el bloque `finally` se ejecuta siempre, sin importar si ocurrió o no una excepción. Este bloque es útil
# para liberar recursos o realizar tareas de limpieza, como cerrar archivos o conexiones a bases de datos.

# Ejemplo Práctico: Captura de NameError
# --------------------------------------
# A continuación, mostramos un ejemplo donde intentamos convertir la entrada del usuario en un número y luego usamos una
# variable no definida, lo que generará un `NameError`.

try:
    # Intentamos convertir la entrada en un número
    numero = int(input("Introduce un número: "))
    ffdssdf  # Esto causará un NameError porque 'ffdssdf' no está definido
except ValueError as error:
    print("Ingrese un valor que corresponda. Ha ocurrido un error de tipo:",
          type(error).__name__)
except NameError as error:
    print("Ha ocurrido un error de tipo:", error)

# En este código:
# - El primer `except` captura errores de tipo `ValueError`, que pueden ocurrir si el usuario ingresa algo que no se puede convertir a un número.
# - El segundo `except` captura `NameError`, que ocurre cuando intentamos usar una variable no definida.
# - El mensaje de error capturado en el `NameError` se imprime en la consola, mostrando por qué ocurrió el error.

# Conclusión
# ==========
# Las excepciones en Python son una herramienta poderosa para manejar errores de manera controlada, permitiendo que el
# programa reaccione de manera adecuada a problemas inesperados. Al aprender a capturar y manejar excepciones de forma
# específica, tus programas serán más robustos y fáciles de depurar.
