# entrar a página para hacer web scraping
# https://stackoverflow.com/questions
# instalar librería beautifulsoup4
# pipenv install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# recibir un string con la url de la página

url = 'https://stackoverflow.com/questions'
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto, 'html.parser')

preguntas = soup.select('.s-post-summary')  # selectores de css

for pregunta in preguntas:
    # print(pregunta.text)
    titulo = pregunta.select_one('.s-link').getText()
    usuario = pregunta.select_one('.s-user-card--link').getText()
    print(f"Usuario: {usuario.strip()} - Pregunta: \n{titulo.strip()}")

# si quiero accder a otras páginas de la misma página
# https://stackoverflow.com/questions?page=2
# print(preguntas[0]["data_post_id"])
