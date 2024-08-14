# Pilas y Colas en Python

# En Python, una pila (stack) se puede implementar usando una lista.
# LIFO (Last In, First Out) es el principio de una pila: el último elemento añadido es el primero en ser retirado.

# Ejemplo: crear una pila
from collections import deque
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)

print("Pila:", pila)

# Para eliminar el último elemento de la pila
ultimo_elemento = pila.pop()

print("Elemento eliminado:", ultimo_elemento)
print("Pila actualizada:", pila)

# Para acceder al último elemento de la pila
print("Último elemento actual:", pila[-1])

if not pila:
    print("La pila está vacía")  # Si la pila está vacía

# Para operaciones más eficientes con grandes cantidades de datos, se recomienda usar deque

# Importamos deque de la librería collections

# Creamos una cola (queue) usando deque
cola = deque([1, 2, 3, 4, 5])

print("\nCola:", cola)

# Para eliminar el primer elemento de la cola
primer_elemento = cola.popleft()

print("Elemento eliminado de la cola:", primer_elemento)
print("Cola actualizada:", cola)

# Para acceder al primer elemento de la cola
print("Primer elemento actual:", cola[0])

if not cola:
    print("La cola está vacía")  # Si la cola está vacía

# Añadir un elemento al final de la cola
cola.append(6)
print("Cola después de añadir un elemento:", cola)
