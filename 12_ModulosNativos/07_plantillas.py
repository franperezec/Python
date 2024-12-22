# crear plantilla html para enviar correos

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Multipurpose Internet
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template  # para plantillas
import smtplib  # Simple Mail Transfer Protocol


# plantilla = """
# <b> Hola, $nombre </b>
# """
# template = Template(plantilla)
# cuerpo = template.substitute({"nombre": "Francisco"}) # diccionario

# path = Path("12_ModulosNativos/imagen.jpg")
# mime_image = MIMEImage(path.read_bytes())
# mensaje = MIMEMultipart()
# mensaje["from"] = "Remitente"
# mensaje["to"] = "CorreoDestino"
# mensaje["subject"] = "Asunto"
# cuerpo_mensaje = MIMEText(cuerpo, "html")
# mensaje.attach(cuerpo_mensaje)
# mensaje.attach(mime_image)

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # puerto 587
#     smtp.ehlo()  # identificar el servidor de correo
#     smtp.starttls()  # cifrado TLS Transport Layer Security
#     smtp.login("tucorreo@gmail.com",
#                "contraseñaaplicacion")  # correo y contraseña
#     smtp.send_message(mensaje)
#     print("Mensaje enviado")

# es mejor usar plantillas html para enviar correos, se crea un archivo html y se pone ! para que se autocomplete en la plantilla html

plantilla = Path("12_ModulosNativos/plantilla.html").read_text()

template = Template(plantilla)
# cuerpo = template.substitute({"nombre": "Francisco"}) # diccionario
cuerpo = template.substitute(nombre="Francisco")

path = Path("12_ModulosNativos/imagen.jpg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Remitente"
mensaje["to"] = "CorreoDestino"
mensaje["subject"] = "Asunto"
cuerpo_mensaje = MIMEText(cuerpo, "html")
mensaje.attach(cuerpo_mensaje)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # puerto 587
    smtp.ehlo()  # identificar el servidor de correo
    smtp.starttls()  # cifrado TLS Transport Layer Security
    smtp.login("tucorreo@gmail.com",
               "contraseña aplicacion")  # correo y contraseña
    smtp.send_message(mensaje)
    print("Mensaje enviado")
