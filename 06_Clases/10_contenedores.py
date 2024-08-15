# Contenedores (objetos que contienen otros objetos)

# Los contenedores son objetos que contienen otros objetos. Algunos ejemplos de contenedores en Python son listas,
# tuplas, conjuntos y diccionarios.

# Los contenedores son útiles para almacenar y organizar datos de manera eficiente. Por ejemplo, una lista puede
# contener varios elementos, mientras que un diccionario puede almacenar pares clave-valor.

# En Python, los contenedores son objetos que implementan los métodos mágicos __len__ y __getitem__.
# Estos métodos mágicos permiten que los contenedores sean indexables y tengan una longitud.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método __str__ para la representación en cadena del objeto Producto
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: (${self.precio})"


class Categoria:
    productos = []  # Lista de productos en la categoría

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    # Método para agregar un producto a la categoría
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para imprimir los productos de la categoría
    def imprimir_productos(self):
        print(f"Productos de la categoría {self.nombre}:")
        for producto in self.productos:
            print(producto)


# Crear algunos productos
balon = Producto("Balón", 20)
raqueta = Producto("Raqueta", 50)
calentador = Producto("Calentador", 10)

# Crear una categoría y agregar los productos
deportes = Categoria("Deportes", [balon, raqueta])
deportes.agregar_producto(calentador)

# Imprimir los productos de la categoría
deportes.imprimir_productos()
