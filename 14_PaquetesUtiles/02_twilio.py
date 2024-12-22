# twilio
# https://www.twilio.com/docs/quickstart/python/sms
# crear cuenta en twilio y obtener credenciales
# pipenv install twilio
# abrir virtualenv

import os
import twilio.rest import Client

sid = os.environ.get('TWILIO_ACCOUNT_SID')
token = os.environ.get('TWILIO_AUTH')
numero = os.environ.get('TWILIO_PHONE')

client = Client(sid, token)
mensaje = client.messages.create(
    to='+15557655310',
    from_=numero,
    body='Hola desde Twilio'
)
