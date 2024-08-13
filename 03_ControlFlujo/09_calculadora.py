# Vamos a crear una calculadora interactiva que  verificque que el usuario ingrese un número y luego realice una operación matemática.
# 1. Solicitar al usuario que ingrese un número
# 2. Solicitar al usuario que ingrese un operador matemático (+, -, *, /)
# 3. Solicitar al usuario que ingrese el siguiente número
# 4. Realizar la operación matemática
# 5. Mostrar el resultado
# 6. Solicitar al usuario que ingrese un operador matemático (+, -, *, /)
# 7. Solicitar al usuario que ingrese el siguiente número
# 8. Realizar la operación matemática
# 9. Mostrar el resultado
# 10. continuar con el proceso hasta que el usuario escriba salir

# Solución 1

print("Bienvenido a la calculadora")
print("Para salir escriba 'salir'")
print("Las operaciones disponibles son: +, -, *, /")
print("")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower == "salir":
            break
        resultado = float(resultado)
    operador = input("Ingrese un operador matemático: ")
    if operador == "salir":
        break
    num = input("Ingrese el siguiente número: ")
    if num.lower() == "salir":
        break
    num = float(num)
    if operador == "+":
        resultado += num
    elif operador == "-":
        resultado -= num
    elif operador == "*":
        resultado *= num
    elif operador == "/":
        resultado /= num
    else:
        print("Operador no válido")
        break
    print(f"El resultado es: {resultado}")
    print("")
print("Gracias por usar la calculadora")


# Solución 2 operaciones matemáticas 1 a 1 con el usuario y se le pregunta si desea continuar o salir
# print("Bienvenido a la calculadora")
# print("Para salir escriba 'salir'")
# print("Las operaciones disponibles son: +, -, *, /")
# print("")


# while True:
#     num1 = input("Ingrese un número: ")
#     if num1 == "salir":
#         break
#     operador = input("Ingrese un operador matemático: ")
#     if operador == "salir":
#         break
#     num2 = input("Ingrese el siguiente número: ")
#     if num2 == "salir":
#         break
#     if operador == "+":
#         resultado = float(num1) + float(num2)
#     elif operador == "-":
#         resultado = float(num1) - float(num2)
#     elif operador == "*":
#         resultado = float(num1) * float(num2)
#     elif operador == "/":
#         resultado = float(num1) / float(num2)
#     else:
#         print("Operador no válido")
#         continue
#     print("El resultado es: ", resultado)
#     print("")

# print("Gracias por usar la calculadora")
