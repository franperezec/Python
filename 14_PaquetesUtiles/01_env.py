# variables de entorno en Python.

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Obtener el valor de una variable de entorno


email = os.environ.get('EMAIL')

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject='Prueba de envío de correo',
    html_content='<strong>Este es un mensaje de prueba</strong>'
)

try:
    api_key = os.environ.get('SENDGRID_API_KEY')
    sg = SendGridAPIClient(api_key)
    response = sg.send(mensaje)
    print(response.status_code)  # 202
    print(response.body)  # cuerpo de la respuesta
    print(response.headers)  # encabezados de la respuesta
except Exception as e:
    print(e)
