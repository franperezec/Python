# While loop
# Un while loop se ejecuta mientras una condición sea verdadera

# podemos usar un while loop para contar hasta 10
contador = 0
while contador < 10:
    print(contador)
    contador += 1

# podemos usar un while loop para llegar hasta 50
contador = 1
while contador < 50:
    print(contador)
    contador *= 2

# podemos usar un while loop para contar hacia atrás
contador = 10
while contador > 0:
    print(contador)
    contador -= 1

# podemos usar un while loop para buscar un número
objetivo = 5
numero = 0
while numero < 10:
    if numero == objetivo:
        print(f"Se encontró el número {objetivo}")
        break
    numero += 1
else:
    print(f"No se encontró el número {objetivo}")

# podemos usar un while loop para leer comandos hasta que se escriba "salir"

comando = ""
while comando.lower() != "salir":
    comando = input("Ingrese un comando: ")
    print(f"Escribiste: {comando}")


# Loops infinitos

# Un loop infinito es un loop que nunca termina por lo que es importante poner condiciones de salida

# podemos hacer un loop infinito con while True
while True:
    print("Este es un loop infinito")
    break

# poner Ctrl + C en la terminal para detener el loop

# podemos hacer un loop infinito con while con condiciones de salida
contador = 0
while contador < 10:
    print(contador)
    if contador == 5:
        break
    contador += 1

# podemos hacer un loop infinito con while con condiciones de salida
contador = 0
while True:
    print(contador)
    if contador == 5:
        break
    contador += 1

# otro ejemplo de loop infinito

while True:
    comando = input("Ingrese un comando: ")
    if comando.lower() == "salir":
        break
    print(f"Escribiste: {comando}")
