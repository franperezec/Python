# Depuración de funciones en Python

# Función original con error
def caracteres_con_error(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
        return resultado  # Error: return dentro del bucle

# Función corregida


def caracteres(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado  # Corrección: return fuera del bucle


# Demostración
print("--- Función con error ---")
print(caracteres_con_error("Hola, mundo!"))  # Devolverá 1

print("\n--- Función corregida ---")
print(caracteres("Hola, mundo!"))  # Devolverá 12

# Instrucciones para depurar en Visual Studio Code:
# 1. Haz clic en "Run and Debug" en la barra lateral izquierda.
# 2. Selecciona "create a launch.json file" y elige "Python File".
# 3. Coloca un punto de interrupción (breakpoint) en la línea del bucle for.
# 4. Haz clic en el botón de play y selecciona "Python File".
# 5. Usa los controles de depuración para avanzar paso a paso y observar los valores de las variables.
# 6. Notarás que en la función con error, el return se ejecuta en la primera iteración del bucle.
# 7. En la función corregida, el bucle se completa antes de llegar al return.

# Ejemplo de uso de la función corregida
texto_ejemplo = "Python es genial!"
longitud = caracteres(texto_ejemplo)
print(f"\nLa longitud de '{texto_ejemplo}' es: {longitud} caracteres")
