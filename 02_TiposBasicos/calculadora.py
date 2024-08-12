numero1 = float(input("Digita el primer número: "))
numero2 = float(input("Digita el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

mensaje = f"""
Para los números {numero1} y {numero2},
el resultado de la suma es: {suma}.
el resultado de la resta es: {resta}.
el resultado de la multiplicación es: {multiplicacion}.
el resultado de la división es: {division}.
"""

print(mensaje)
