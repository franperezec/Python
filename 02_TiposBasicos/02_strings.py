nombre_persona = "Francisco"
direccion = """"Calle 123,
Colonia Centro, Quito"""
print(nombre_persona, direccion)

len(nombre_persona)  # longitud del estring es 9, argumento es nombre_persona
print(len(nombre_persona))

print(nombre_persona[0])  # F, 0 es el primer caracter
# quiero solo ciertos caracteres, 0:7 es el rango de caracteres
print(direccion[0:7])
print(direccion[9:])  # desde el caracter 9 hasta el final
print(direccion[:7])  # desde el inicio hasta el caracter 7
print(direccion[-5:])  # los últimos 5 caracteres
print(direccion[:-5])  # desde el inicio hasta los últimos 5 caracteres
print(direccion[::2])  # desde el inicio hasta el final, saltando de 2 en 2
print(direccion[:])  # desde el inicio hasta el final
