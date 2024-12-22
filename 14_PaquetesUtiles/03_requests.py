# Requests es una librería de Python que permite enviar solicitudes HTTP/1.1
# de una manera sencilla.

import requests

# Ejemplo básico
# response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.text)

# API Rest significa que se puede hacer peticiones a un servidor y obtener
# una respuesta en formato JSON.
# En este caso, la respuesta es un JSON con información sobre la API de GitHub.
# La respuesta es un objeto Response de requests, que tiene varios atributos
# y métodos útiles.
# - status_code: indica el código de estado de la respuesta
# - text: contiene el contenido de la respuesta en texto plano
# - json(): método para obtener un diccionario de Python si
# la respuesta es JSON

# Métodos HTTP comunes:
# - GET: obtener información de un servidor
# - POST: enviar información a un servidor
# - PUT: actualizar información en un servidor
# - DELETE: eliminar información de un servidor
# - HEAD: obtener la cabecera de una respuesta
# - OPTIONS: obtener información sobre métodos permitidos
# - PATCH: aplicar modificaciones parciales a un recurso

# Códigos de estado comunes:
# - 200: solicitud exitosa (GET)
# - 201: recurso creado exitosamente (POST)
# - 204: solicitud exitosa sin contenido (DELETE, PUT, PATCH)

# Ejemplo con JSONPlaceholder API
base_url = 'https://jsonplaceholder.typicode.com'

# Obtener todos los usuarios
users_url = f'{base_url}/users'
response = requests.get(users_url, timeout=5)
print(response.status_code)

# Imprimir nombres de usuarios
users = response.json()
for user in users:
    print(user['name'])

# Obtener un usuario específico
user_url = f'{base_url}/users/1'
response = requests.get(user_url, timeout=5)
print(response.status_code)
print(response.json())

# Crear un nuevo usuario
new_user = {"name": "Leanne Graham"}
response = requests.post(users_url, json=new_user)
print(response.status_code)  # 201

# Actualizar un usuario
update_url = f'{base_url}/users/1'
updated_user = {"name": "Leanne Graham"}
response = requests.put(update_url, json=updated_user)
print(response.status_code)  # 200

# Eliminar un usuario
delete_url = f'{base_url}/users/4'
response = requests.delete(delete_url)
print(response.status_code)  # 200
