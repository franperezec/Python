# Importa el módulo 'requests'
import requests

# Realiza una solicitud GET a la página principal de Google
r = requests.get("https://www.google.com")

# Imprime el código de estado de la respuesta HTTP
# Un código de estado 200 indica que la solicitud ha sido exitosa y el servidor ha respondido correctamente.
print(r.status_code)  # 200 means OK
