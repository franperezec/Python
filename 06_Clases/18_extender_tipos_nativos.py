# Extender tipos nativos
# =======================

# En Python, es posible extender los tipos nativos de la misma manera que se extienden las clases. Esto significa que puedes agregar nuevos métodos y atributos a tipos de datos como listas, diccionarios, cadenas, etc.

# Por ejemplo, supongamos que deseas agregar un método `duplicar` a la clase `list` que duplique todos los elementos de la lista. Puedes hacerlo de la siguiente manera:

lista = list([1, 2, 3, 4, 5])

# si pongo punto luego de lista, me aparecen los métodos que puedo usar con listas por ejemplo append
lista.append(6)

lista.insert(0, 0)

print(lista)  # [0, 1, 2, 3, 4, 5, 6]

# class Lista podemos extender la clase list podemos hacer con strings, diccionarios, etc


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3, 4, 5])
lista.prepend(0)
print(lista)  # [0, 1, 2, 3, 4, 5]


# # Extender Tipos Nativos
# # =======================
# # En Python, es posible extender los tipos nativos de la misma manera que se extienden las clases.
# # Esto significa que puedes agregar nuevos métodos y atributos a tipos de datos como listas, diccionarios,
# # cadenas, etc. Esto te permite personalizar el comportamiento de los tipos nativos y añadir funcionalidades
# # adicionales que pueden ser útiles para casos específicos.

# # Ejemplo: Extender la Clase `list`
# # ---------------------------------
# # Supongamos que deseas agregar un método `prepend` a la clase `list` que inserte un elemento al inicio
# # de la lista. Puedes hacerlo creando una nueva clase que herede de `list` y luego agregando el nuevo
# # método a esa clase.

# # Crear una instancia básica de la clase `list`
# lista = list([1, 2, 3, 4, 5])

# # Utilizando los métodos nativos de `list`
# # ----------------------------------------
# # El objeto `lista` puede usar todos los métodos disponibles para listas en Python.
# # Por ejemplo, puedes agregar un elemento al final de la lista usando `append` y
# # agregar un elemento en una posición específica usando `insert`.

# # Añadir un elemento al final de la lista
# lista.append(6)

# # Insertar un elemento al inicio de la lista
# lista.insert(0, 0)

# # Imprimir la lista actualizada
# print(lista)  # Salida: [0, 1, 2, 3, 4, 5, 6]

# # Extender la Clase `list`
# # ------------------------
# # Ahora, extenderemos la clase `list` para agregar un nuevo método llamado `prepend`.
# # Este método insertará un elemento al inicio de la lista, simulando la operación de
# # agregar un elemento "antes" de todos los demás.

# class Lista(list):
#     def prepend(self, item):
#         """
#         Inserta un elemento al inicio de la lista.
#         Este método es una extensión personalizada de la clase `list`.
#         """
#         self.insert(0, item)

# # Crear una instancia de la clase extendida `Lista`
# lista = Lista([1, 2, 3, 4, 5])

# # Usar el nuevo método `prepend` para agregar un elemento al inicio de la lista
# lista.prepend(0)

# # Imprimir la lista actualizada utilizando el nuevo método
# print(lista)  # Salida: [0, 1, 2, 3, 4, 5]

# # Análisis y Aplicaciones
# # -----------------------
# # Al extender tipos nativos como `list`, puedes agregar comportamientos específicos que sean útiles
# # para tu aplicación. En este ejemplo, la clase `Lista` hereda todas las funcionalidades de la clase
# # nativa `list`, pero además incluye un método adicional `prepend` que permite insertar elementos
# # al inicio de la lista de una manera más directa y conveniente.

# # Este enfoque puede ser utilizado para extender otros tipos nativos en Python, como `str`, `dict`,
# # `set`, etc. Puedes crear clases que hereden de estos tipos y agregar métodos personalizados que
# # realicen operaciones comunes en tu aplicación, reduciendo la repetición de código y mejorando la
# # legibilidad y mantenibilidad de tu código.
