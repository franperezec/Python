# Cadena de comparadores
# La cadena de comparadores es una técnica que nos permite evaluar múltiples
# comparaciones en una sola línea de código. Para ello, se utilizan los
# operadores de comparación y los operadores lógicos and y or. La cadena de
# comparadores se evalúa de izquierda a derecha, y se detiene en el primer
# valor que determine el resultado de la expresión.

# Ejemplo de cadena de comparadores
ingresos = 1000
gastos = 800
ahorro = 200
if ingresos > gastos > ahorro:
    print("Tienes un buen ahorro")
else:
    print("Debes ahorrar más")

# En este caso, la cadena de comparadores se evalúa de izquierda a derecha.

ingresos = 450

if 0 < ingresos < 1000:
    print("Tus ingresos son bajos")  # Se imprime

# esta lógica es equivalente a la siguiente:
if ingresos > 0 and ingresos < 1000:
    print("Tus ingresos son bajos")  # Se imprime
