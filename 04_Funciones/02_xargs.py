# xargs
# xargs es un comando de Unix y sistemas operativos similares que construye y ejecuta comandos de línea de comandos a partir de la entrada estándar.

# esto nos limita a tener que definir la cantidad de argumentos que recibe una función
def suma(a, b):
    print(a + b)


suma(2, 3)  # 5

# xargs nos permite pasar una cantidad variable de argumentos a una función

# podemos pasar una cantidad variable de argumentos a una función con el símbolo * y sin necesidad de definir una tupla


def suma1(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)  # imprimimos el resultado de la suma ponerlo a este nivel de indentación es importante porque si no se imprimirá en cada iteración del bucle


suma1(2, 3)  # 5
suma1(2, 3, 4)  # 9
suma1(2, 3, 4, 5)  # 14


def suma2(*args):  # args es una tupla con los argumentos que recibe la función el símbolo * indica que la cantidad de argumentos es variable
    # sum es una función de Python que suma todos los elementos de una lista
    print(sum(args))


suma2(2, 3)  # 5
suma2(2, 3, 4)  # 9
suma2(2, 3, 4, 5)  # 14
