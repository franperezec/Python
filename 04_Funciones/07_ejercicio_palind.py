# def es_palin(texto):
#     texto = texto.replace(" ", "").lower()
#     return texto == texto[::-1]


# print(es_palin("Anita lava la tina"))
# print(es_palin("Hola mundo"))
# print(es_palin("amo la paloma"))
# print("Reconocer", es_palin("Reconocer"))

# otra forma de hacerlo
# 1. eliminas los espacios en blanco

def no_espacios(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_espacios(texto)
    texto_al_reves = reverse(texto)
    print(texto)
    print(texto_al_reves)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola mundo"))
print(es_palindromo("amo la paloma"))
print(es_palindromo("Reconocer"))
print(es_palindromo(
    "A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá"))
print(es_palindromo("A ti no bonita"))


# Ctrl + Shift + L -> seleccionar todas las ocurrencias
# Ctrl + D -> seleccionar la siguiente ocurrencia
