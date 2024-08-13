# Tema: Estructuras de control de flujo
edad = 18
if edad >= 18:
    # hay que tener en cuenta la indentación 4 espacios
    print("Eres mayor de edad")
# else: de lo contrario
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# elif: de lo contrario si, el código se lee de arriba hacía abajo y se ejecuta la primera condición que se cumpla
edad = 18
if edad >= 65:  # si edad es mayor o igual a 65 se ejecuta primero
    print("Eres adulto mayor")
elif edad > 17:  # si edad es mayor a 17 se ejecuta segundo
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# otros ejemplos
edad = 18
if edad >= 65:  # si edad es mayor o igual a 65 se ejecuta primero
    print("Eres adulto mayor")
elif edad > 35:  # si edad es mayor a 35 se ejecuta segundo
    print("Eres adulto")
elif edad > 17:  # si edad es mayor a 17 se ejecuta segundo
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# atajos teclado VSC para comentar y descomentar código
# Ctrl + K + C (comentar)
# Ctrl + K + U (descomentar)
