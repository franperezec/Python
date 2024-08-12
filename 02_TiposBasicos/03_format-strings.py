nombre = "Francisco"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido  # Concatenación de strings
print(nombre_completo)

# otra forma de concatenar strings
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)

# mostrar el primer caracter y un identificador
print(f"{nombre_completo[0]} es el primer caracter de {nombre_completo} {1+2}")
