# # app.py
# # ======
# # En este archivo, importamos y utilizamos las funciones definidas en el módulo `usuario_tarjeta`.
# # Importar solo lo necesario mejora la legibilidad y eficiencia del código.

# # Es recomendable utilizar la combinación de teclas Ctrl + Espacio en algunos entornos de desarrollo
# # para desplegar opciones de importación. Esto facilita encontrar y seleccionar exactamente lo que necesitas.

# from usuario_tarjeta import guardar, pagar_tarjeta

# # Importamos y utilizamos las funciones específicas del módulo `usuario_tarjeta`.
# # Es preferible importar solo las funciones que realmente necesitas, en lugar de usar `import *`,
# # lo que podría importar todo el contenido del módulo. Importar solo lo necesario:
# # 1. Mejora la legibilidad del código, ya que es más fácil ver qué funciones están en uso.
# # 2. Reduce el riesgo de conflictos de nombres.
# # 3. Aumenta la eficiencia, ya que solo se carga en memoria lo necesario.

# # Llamamos a la función `guardar` para simular la acción de guardar un usuario.
# guardar()

# # Llamamos a la función `pagar_tarjeta` para simular la acción de realizar un pago con tarjeta.
# pagar_tarjeta()

# # Nota importante: Si no importas una función específica del módulo, no podrás utilizarla en este archivo.
# # Por ejemplo, si comentas la línea `from usuario_tarjeta import pagar_tarjeta`, la siguiente llamada generará un error:
# # pagar_tarjeta()  # Esto causará un NameError si `pagar_tarjeta` no está importada.


# ---------------------------

# importar paquete

# from usuarios.acciones import pagar_impuestos  # Importamos la función `pagar_impuestos` del módulo `usuarios.acciones`.
# # esta es una forma de importar una funcion especifica de un modulo
# # Llamamos a la función `pagar_impuestos` para simular la acción de pagar impuestos.
# # podemos llama a todas las funciones de un modulo
# # from usuarios import acciones

# # pagar_impuestos()

# Otra forma de importar una función específica de un módulo es utilizando la siguiente sintaxis:
# # Importamos el módulo `usuarios.acciones` con un alias `acciones`.
# import usuarios.acciones as acciones

# # Llamamos a la función `pagar_impuestos` del módulo `usuarios.acciones` utilizando el alias.
# acciones.pagar_impuestos()


# ---------------------------

# importar subpaquete

# from usuarios.actividades.actividad import realizar_actividad

# # Llamamos a la función `realizar_actividad` del módulo `usuarios.acciones.actividad`.
# realizar_actividad()


# si muestra errores reiniciar el entorno de desarrollo o la terminal


# # ---------------------------
# # referenciando subpaquetes

# from usuarios.impuestos.renta import impuesto_renta

# # Llamamos a la función `impuesto_renta` del módulo `usuarios.impuestos.renta`.
# impuesto_renta()

# # # ---------------------------
# #  dir
# from usuarios.impuestos.renta import impuesto_renta
# import usuarios
# # Muestra una lista de los atributos y métodos del módulo `usuarios.acciones`.
# # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'acciones', 'actividades', 'gestion', 'impuestos']
# # se listan los modulos que estan dentro de usuarios y los métodos más importantes
# print(dir(usuarios))

# print(usuarios.__file__)  # muestra la ruta del archivo
# print(usuarios.__package__)  # muestra el paquete
# print(usuarios.__path__)  # muestra la ruta del paquete
# print(usuarios.__name__)  # muestra el nombre del paquete

# # # ---------------------------

# # paquetes con nombres dinámicos
# from usuarios.impuestos.renta import impuesto_renta

# impuesto_renta()

# # Muestra el nombre del módulo actual. # __main__ dependiendo cómo se está ejecutando el archivo
# print(__name__)


# # ---------------------------

# import condicionados
from usuarios.impuestos.renta import impuesto_renta

impuesto_renta()

# Muestra el nombre del módulo actual. # __main__ dependiendo cómo se está ejecutando el archivo
