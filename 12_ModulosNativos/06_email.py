# Enviar correos electrónicos con Python
# activar aplicaciones menos seguras
# "https://myaccount.google.com/u/1/lesssecureapps"
# en Gmail Allow less secure apps:  esto se deshabilitad desde sept 2024
# otra forma es con App passwords https://myaccount.google.com/apppasswords
# crear una contraseña de aplicación

# otros protocolos: IMAP, POP3 un poco más antiguos
# sendgrid, mailgun, mailchimp, etc. para enviar correos masivos
# Multipurpose Internet Mail Extensions
# Multipurpose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Multipurpose Internet
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib  # Simple Mail Transfer Protocol

path = Path("12_ModulosNativos/imagen.jpg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Remitente"
mensaje["to"] = "correoDestino"
mensaje["subject"] = "Asunto"
cuerpo_mensaje = MIMEText("Contenido del mensaje", "plain")
mensaje.attach(cuerpo_mensaje)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # puerto 587
    smtp.ehlo()  # identificar el servidor de correo
    smtp.starttls()  # cifrado TLS Transport Layer Security
    smtp.login("tucorreo@gmail.com",
               "contraseña aplicación")  # correo y contraseña
    smtp.send_message(mensaje)
    print("Mensaje enviado")

# #Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
# --     ----            -------------   -----         -----------     --------             -------
# 1      Job1            BackgroundJob   Running       True            localhost            https://support.google.c…
# Mensaje enviado
