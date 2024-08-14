# Implementación de una clase en Python

# Definición de la clase OperacionesMatematicas

class OperacionesMatematicas:  # se usa PascalCase o UpperCamelCase para el nombre de la clase
    def suma(self, a, b):  # método suma  #self es una referencia al objeto actual de la clase a, b son los parámetros
        return a + b  # devuelve la suma de a y b


# instanciación de la clase OperacionesMatematicas (PascalCase diferencia a las funciones) principal razón de usar clases y objetos
mi_operacion = OperacionesMatematicas()

# <class '__main__.OperacionesMatematicas'> es un objeto de la clase OperacionesMatematicas
print(type(mi_operacion))

# 8 # se llama al método suma de la clase OperacionesMatematicas
mi_operacion.suma(5, 3)

# True mi_operacion es una instancia de la clase OperacionesMatematicas

# True mi_operacion es una instancia de la clase OperacionesMatematicas
print(isinstance(mi_operacion, OperacionesMatematicas))
# False mi_operacion no es una instancia de la clase str
print(isinstance(mi_operacion, str))

# Definición de la clase OperacionesMatematicas

# class OperacionesMatematicas:  # se usa PascalCase o UpperCamelCase para el nombre de la clase
#     def suma(self, a, b):  # método suma  #self es una referencia al objeto actual de la clase a, b son los parámetros
#         return a + b  # devuelve la suma de a y b

#     def resta(self, a, b):  # método resta
#         return a - b  # devuelve la resta de a y b

#     def multiplicacion(self, a, b):  # método multiplicación
#         return a * b  # devuelve la multiplicación de a y b

#     def division(self, a, b):  # método división
#         return a / b  # devuelve la división de a y b
