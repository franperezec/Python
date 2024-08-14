# Filas en Python

# En Python, una fila es una secuencia de elementos separados por comas y encerrados entre corchetes [].

# Ejemplo: crear una fila

from collections import deque
fila = [1, 2, 3, 4, 5]

# FIFO: First In, First Out
fila = [1, 2, 3, 4, 5]

# añadir un elemento al final de la fila
fila.append(6)

# pero si tenemos 10000000 es más eficiente usar un deque


# se crea una columna con los elementos 1, 2, 3, 4 y 5
columna = deque([1, 2, 3, 4, 5])
columna.append(6)  # se añade el elemento 6 al final de la columna

columna.popleft()  # se elimina el primer elemento de la columna

if not columna:  # si la columna está vacía
    print("La columna está vacía")


# LIFO: Last In, First Out
