# Operadores lógicos en Python
# Los operadores lógicos son aquellos que nos permiten realizar operaciones
# de comparación entre dos valores booleanos. Los operadores lógicos en Python
# son los siguientes:
# and: Devuelve True si ambos valores son True.
# or: Devuelve True si al menos uno de los valores es True.
# not: Devuelve True si el valor es False.
# Ejemplo de operador and
# print(True and True)  # True
# print(True and False)  # False

# Ejemplo de operador or
# print(True or False)  # True

""" Vamos a escribir un programa para usar los operadores lógicos en Python
para un semáforo y cuándo debemos cruzar la calle"""


from datetime import datetime
luz_roja = False  # si es True, un peatón puede cruzar
carros_quietos = False  # si es True, un peatón puede cruzar
luz_verde = True  # si es True, un peatón no puede cruzar
no_hay_carros = False  # si es True, un peatón puede cruzar

if no_hay_carros:
    print("Puedes cruzar la calle")
elif luz_roja and (carros_quietos or not luz_verde):
    print("Puedes cruzar la calle")
else:
    print("No puedes cruzar la calle")


""" Vamos a escribir un programa que nos diga la hora actual y 
si es de día o de noche, si es de noche nos dirá que debemos prender la luz"""
hora_actual = datetime.now()
hora = hora_actual.hour
if 6 <= hora < 18:
    if hora_actual.minute < 10:
        print(f"Es de día, son las {hora_actual.hour}:0{
              hora_actual.minute} horas, no es necesario prender la luz")
    else:
        print(f"Es de día, son las {hora_actual.hour}:{
              hora_actual.minute} horas, no es necesario prender la luz")
else:
    if hora_actual.minute < 10:
        print(f"Es de noche, son las {hora_actual.hour}:0{
              hora_actual.minute} horas, prende la luz")
    else:
        print(f"Es de noche, son las {hora_actual.hour}:{
              hora_actual.minute} horas, prende la luz")

# Operadores de corto-circuito

# Los operadores de corto-circuito son aquellos que no evalúan todas las
# condiciones de una expresión lógica si no es necesario. En Python, los
# operadores de corto-circuito son los siguientes:
# and: Si el primer valor es False, no evalúa el segundo valor.
# or: Si el primer valor es True, no evalúa el segundo valor.
# estos operadores nos permiten optimizar el rendimiento de nuestro
# programa, ya que si el primer valor es suficiente para determinar el
# resultado de la expresión, no es necesario evaluar el segundo valor.


# Ejemplo de operador and con corto-circuito

print(False and True and True)  # False

# Ejemplo de operador or con corto-circuito
print(True or False or False)  # True

# Ejemplo de operador and con corto-circuito
print(False and True and False)  # False

# Ejemplo de operador or con corto-circuito
print(True or True or False)  # True
