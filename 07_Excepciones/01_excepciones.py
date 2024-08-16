# Introducción a las Excepciones en Python
# ========================================

# En programación, es común encontrarse con situaciones donde algo inesperado ocurre, como un error al intentar
# convertir un string en un número, o un intento de acceder a un índice fuera del rango en una lista.
# Estas situaciones generan "excepciones". Una excepción es un evento que interrumpe el flujo normal de la ejecución
# de un programa cuando algo sale mal.

# Excepciones en Python
# =====================
# Las excepciones en Python son una forma de manejar errores de manera controlada. En lugar de que el programa se
# detenga abruptamente cuando ocurre un error, puedes usar excepciones para "atrapar" ese error y decidir qué hacer
# en respuesta. Esto hace que tu programa sea más robusto y resistente a fallos inesperados.

# Cuando se produce una excepción, Python detiene la ejecución normal del programa y arroja un mensaje de error.
# Sin embargo, usando las herramientas adecuadas, podemos manejar estas excepciones para que el programa siga
# funcionando o al menos, finalice de una manera más controlada.

# Ejemplos de Excepciones Comunes
# ===============================
# Hay muchos tipos de excepciones en Python, cada una correspondiente a diferentes tipos de errores.

# 1. **SyntaxError**: Ocurre cuando hay un error de sintaxis en el código.
#    Por ejemplo, si te olvidas de cerrar un paréntesis, obtendrás un SyntaxError.
#    Código incorrecto:
#    print("")   # Aquí falta el paréntesis de cierre

# 2. **IndexError**: Sucede cuando intentas acceder a un índice que está fuera del rango en una lista.
#    Código incorrecto:
#    lista = [1, 2, 3]
#    print(lista[4])  # La lista solo tiene 3 elementos, el índice 4 no existe.

# 3. **ValueError**: Aparece cuando intentas convertir un tipo de dato a otro incorrectamente.
#    Por ejemplo, intentar convertir una cadena de texto que no representa un número en un entero.
#    Esto es especialmente relevante cuando recibes entrada del usuario.

# Manejo de Excepciones con `try-except`
# ======================================
# Para manejar excepciones y evitar que nuestro programa se detenga abruptamente, usamos las sentencias `try` y `except`.
# - El bloque `try` contiene el código que queremos ejecutar normalmente.
# - El bloque `except` contiene el código que se ejecutará si ocurre una excepción durante la ejecución del bloque `try`.

# Ejemplo Práctico
# ================
# A continuación, mostramos cómo manejar un `ValueError` cuando el usuario ingresa un dato incorrecto.

try:
    # Intentamos convertir la entrada del usuario a un número entero
    numero1 = int(input("Ingrese un número: "))
except ValueError:  # Capturamos específicamente el error de tipo ValueError
    # Si ocurre un ValueError, mostramos un mensaje al usuario indicando el error
    print("Ha ocurrido un error, por favor ingrese un número válido")

# Explicación del Código:
# =======================
# 1. **try**: El código dentro del bloque `try` es donde esperamos que ocurra un error. En este caso, estamos intentando
#    convertir una entrada del usuario a un número entero. Si el usuario ingresa un valor que no se puede convertir (como una letra),
#    Python arrojará una excepción de tipo `ValueError`.

# 2. **except ValueError**: Aquí especificamos que queremos capturar y manejar específicamente un `ValueError`. Esto es una
#    buena práctica, ya que estamos siendo explícitos sobre qué error estamos esperando. Si ocurre un `ValueError`,
#    Python ejecutará el código dentro de este bloque `except`, donde simplemente mostramos un mensaje de error al usuario.

# Importancia de Capturar Excepciones Específicas
# ===============================================
# Es importante capturar excepciones específicas en lugar de capturar cualquier excepción de manera genérica. Esto no solo
# hace tu código más claro y fácil de mantener, sino que también asegura que no estarás ocultando otros errores que no
# anticipaste. Al capturar solo las excepciones que esperas y sabes cómo manejar, puedes asegurarte de que el programa
# reacciona de la mejor manera posible ante errores específicos.

# Ventajas del Manejo de Excepciones
# ==================================
# 1. **Robustez**: Permite que tu programa siga funcionando, incluso cuando ocurre un error inesperado.
# 2. **Mejor Experiencia de Usuario**: En lugar de que el programa se cierre abruptamente, puedes mostrar mensajes
#    amigables al usuario, pidiéndole que intente de nuevo.
# 3. **Depuración y Mantenimiento**: Capturar excepciones específicas facilita la identificación y corrección de errores en el código.

# Resumen:
# ========
# Las excepciones son una herramienta poderosa en Python que te permite manejar errores de manera controlada.
# Con `try` y `except`, puedes interceptar errores potenciales y tomar medidas para evitar que el programa falle
# de manera inesperada. Al enseñar a tus alumnos sobre excepciones, estarás dotándolos de una habilidad esencial
# para escribir código más sólido y preparado para el mundo real.
