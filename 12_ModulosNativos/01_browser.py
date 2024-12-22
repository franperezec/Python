# # browser module

# import webbrowser

# print("producto encontrado")
# webbrowser.open("https://www.google.com")

import webbrowser  # Importamos el módulo webbrowser para abrir navegadores web


def buscar_producto(producto):
    """
    Función para buscar un producto en diferentes sitios web.
    Toma como argumento el nombre del producto a buscar.
    """
    # Diccionario que contiene los sitios web y las URLs construidas dinámicamente para buscar el producto
    sitios_web = {
        # URL de búsqueda en Google
        "Google": f"https://www.google.com/search?q={producto}",
        # URL de búsqueda en Amazon
        "Amazon": f"https://www.amazon.com/s?k={producto}",
        # URL de búsqueda en eBay
        "eBay": f"https://www.ebay.com/sch/i.html?_nkw={producto}",
    }

    # Imprimimos un mensaje indicando que se está buscando el producto en diferentes sitios web
    print(f"Buscando '{producto}' en los siguientes sitios web:")

    # Iteramos sobre cada sitio web en el diccionario sitios_web
    for nombre, url in sitios_web.items():
        # Imprimimos el nombre del sitio web y la URL que se abrirá
        print(f"Abrir {nombre}: {url}")
        # Utilizamos webbrowser.open(url) para abrir el navegador web en la URL especificada
        webbrowser.open(url)


# Ejemplo de uso de la función buscar_producto
producto = "teclado mecánico"  # Definimos el nombre del producto a buscar
# Llamamos a la función buscar_producto con el nombre del producto
buscar_producto(producto)
