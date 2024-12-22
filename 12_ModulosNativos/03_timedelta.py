# Uso de timedelta para manipular fechas y horas en Python

# Importamos las clases necesarias del módulo datetime
from datetime import datetime, timedelta

# 1. Creación y comparación de fechas
print("1. Creación y comparación de fechas")
fecha1 = datetime(2023, 5, 25)  # Creamos una fecha (25 de mayo de 2023)
fecha2 = datetime(2021, 5, 30)  # Creamos otra fecha (30 de mayo de 2021)

# Calculamos la diferencia entre las fechas
diferencia = fecha1 - fecha2
print("Diferencia entre fechas:", diferencia)
print("Días de diferencia:", diferencia.days)
print("Segundos de diferencia:", diferencia.seconds)
print("Microsegundos de diferencia:", diferencia.microseconds)
print("Total de segundos de diferencia:", diferencia.total_seconds())
print()

# 2. Uso de timedelta para añadir tiempo a una fecha
print("2. Uso de timedelta para añadir tiempo a una fecha")
fecha3 = datetime(2021, 5, 30) + timedelta(days=7)  # Sumamos 7 días a la fecha
print("Fecha original: 2021-05-30")
print("Fecha después de sumar 7 días:", fecha3)
print()

# 3. Trabajando con la fecha y hora actual
print("3. Trabajando con la fecha y hora actual")
fecha_actual = datetime.now()  # Obtenemos la fecha y hora actual
print("Fecha y hora actual:", fecha_actual)

# Sumamos 7 días a la fecha actual utilizando timedelta
fecha_futura = fecha_actual + timedelta(days=7)
print("Fecha y hora en una semana:", fecha_futura)

# Calculamos la diferencia entre la fecha actual y una fecha específica
fecha_cumple = datetime(2003, 5, 25)  # Creamos una fecha de cumpleaños
diferencia = fecha_actual - fecha_cumple
print("Días desde el cumpleaños (25/05/2003):", diferencia.days)
print()

# 4. Uso de timedelta para restar tiempo
print("4. Uso de timedelta para restar tiempo")
fecha_pasada = fecha_actual - timedelta(hours=2)
print("Fecha y hora actual:", fecha_actual)
print("Fecha y hora hace dos horas:", fecha_pasada)
print()

# 5. Función para calcular la edad
print("5. Función para calcular la edad")


def calcular_edad(fecha_nacimiento):
    """
    Función para calcular la edad de una persona a partir de su fecha de nacimiento.

    Argumentos:
    fecha_nacimiento -- una cadena con la fecha de nacimiento en formato "dd/mm/aaaa"

    Retorna:
    La edad de la persona en años (int)
    """
    # Convertimos la cadena de fecha de nacimiento a un objeto datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    # Obtenemos la fecha actual
    fecha_actual = datetime.now()
    # Calculamos la diferencia entre la fecha actual y la fecha de nacimiento
    diferencia = fecha_actual - fecha_nacimiento
    # Calculamos la edad en años redondeando hacia abajo
    edad = diferencia.days // 365
    return edad


# Ejemplo de uso de la función calcular_edad
print("Edad de la persona nacida el 25/05/2003:", calcular_edad("25/05/2003"))

# Este código demuestra cómo trabajar con fechas y horas en Python utilizando
# los módulos datetime y timedelta. Experimenten cambiando las fechas y los
# intervalos de tiempo para ver cómo afecta a los resultados.
