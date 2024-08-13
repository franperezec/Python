# otra forma de pasar una cantidad variable de argumentos a una función es con el símbolo ** keyword arguments

# kwargs ejemplo 1

def get_product(**datos):
    print(datos)
    print(datos['nombre'])


get_product(nombre='Camisa', precio=50)  # {'nombre': 'Camisa', 'precio': 50}


# ejemplo 2 de kwargs

def suma(**kwargs):  # kwargs es un diccionario con los argumentos que recibe la función el símbolo ** indica que la cantidad de argumentos es variable
    print(kwargs)  # kwargs es un dic
    print(sum(kwargs.values()))  # sumamos los valores del diccionario kwargs


suma(a=2, b=3)  # 5
suma(a=2, b=3, c=4)  # 9
