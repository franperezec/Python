# Importamos el módulo datetime para trabajar con fechas y horas
from datetime import datetime

# Obtenemos la fecha y hora actual
fecha_actual = datetime.now()
print("Fecha y hora actual:", fecha_actual)

# Creamos una fecha de cumpleaños específica
fecha_cumple = datetime(2003, 5, 25)

# Calculamos la diferencia entre la fecha actual y la fecha de cumpleaños
diferencia = fecha_actual - fecha_cumple
print("Días desde mi cumpleaños:", diferencia.days)

# Formateamos la fecha actual en un formato específico
fecha_formateada = fecha_actual.strftime("%A, %d de %B de %Y")
print("Fecha formateada:", fecha_formateada)

# Directivas de formato para strftime y strptime
# %Y: Año con cuatro dígitos
# %m: Mes con dos dígitos (01-12)
# %d: Día del mes con dos dígitos (01-31)
# %H: Hora en formato de 24 horas (00-23)
# %M: Minutos con dos dígitos (00-59)
# %S: Segundos con dos dígitos (00-59)
# %A: Nombre completo del día de la semana (por ejemplo, 'Monday')
# %B: Nombre completo del mes (por ejemplo, 'January')
# %a: Nombre corto del día de la semana (por ejemplo, 'Mon')
# %b: Nombre corto del mes (por ejemplo, 'Jan')

# Convertimos una cadena de texto a un objeto datetime
fechaString = "25/05/2003"
fecha_cumple2 = datetime.strptime(fechaString, "%d/%m/%Y")
print("Fecha de cumpleaños:", fecha_cumple2)

# Convertimos un objeto datetime a una cadena de texto
print(fecha_cumple2.strftime("%d/%m/%Y"))  # 25/05/2003

# Comparamos fechas
fecha1 = datetime(2021, 5, 25)
fecha2 = datetime(2021, 5, 30)

if fecha1 < fecha2:
    print("fecha1 es anterior a fecha2")
else:
    print("fecha1 es posterior a fecha2")

print(fecha1 < fecha2)  # True

# Accedemos a los componentes individuales de una fecha
print(
    fecha1.year,
    fecha1.month,
    fecha1.day,
    fecha1.hour,
    fecha1.minute
)
