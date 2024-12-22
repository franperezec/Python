# Números aleatorios en Python

# Importamos los módulos necesarios
import random
import string

# 1. Generación de números aleatorios básicos
print("1. Generación de números aleatorios básicos")

# Generamos un número decimal aleatorio entre 0 y 1
numero_aleatorio = random.random()
print("Número aleatorio entre 0 y 1:", numero_aleatorio)

# Generamos un número entero aleatorio entre 0 y 9 (inclusive)
numero_aleatorio_entre = random.randint(0, 9)
print("Número aleatorio entre 0 y 9:", numero_aleatorio_entre)

print()

# 2. Selección aleatoria de elementos
print("2. Selección aleatoria de elementos")

# Lista de elementos para elegir aleatoriamente
elementos = ["rojo", "azul", "verde", "amarillo", "naranja"]

# Elegimos un elemento aleatorio de la lista
elemento_aleatorio = random.choice(elementos)
print("Elemento aleatorio de la lista:", elemento_aleatorio)

# Elegir varios elementos aleatorios de la lista (con posible repetición)
elementos_aleatorios = random.choices(elementos, k=3)
print("Varios elementos aleatorios de la lista (con posible repetición):",
      elementos_aleatorios)

# Elegir varios elementos aleatorios de la lista sin repetición
elementos_aleatorios_sin_repeticion = random.sample(elementos, k=3)
print("Varios elementos aleatorios sin repetición:",
      elementos_aleatorios_sin_repeticion)

print()

# 3. Mezclado aleatorio de listas
print("3. Mezclado aleatorio de listas")

# Hacemos una copia de la lista original para no modificarla
elementos_para_mezclar = elementos.copy()

# Mezclamos los elementos de la lista
random.shuffle(elementos_para_mezclar)
print("Lista de elementos mezclada:", elementos_para_mezclar)

print()

# 4. Selección aleatoria de caracteres
print("4. Selección aleatoria de caracteres")

# Seleccionamos 3 caracteres aleatorios de una cadena
caracteres_aleatorios = random.choices("abcdoksdjklfj", k=3)
print("3 caracteres aleatorios de una cadena:", caracteres_aleatorios)

print()

# 5. Generación de contraseña aleatoria
print("5. Generación de contraseña aleatoria")

# Longitud de la contraseña
longitud = 8

# Caracteres a utilizar para generar la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generamos la contraseña aleatoria
password = ''.join(random.choices(caracteres, k=longitud))
print("Contraseña aleatoria:", password)

print()

# 6. Uso de semilla para reproducibilidad
print("6. Uso de semilla para reproducibilidad")

# La función random.seed() se utiliza para inicializar el generador de números aleatorios con una semilla específica.
# Esto permite reproducir la misma secuencia de números "aleatorios".

# Inicializamos el generador de números aleatorios con una semilla específica
random.seed(42)

# Generamos un número entero aleatorio entre 0 y 9
numero_aleatorio_con_semilla = random.randint(0, 9)
print("Número aleatorio entre 0 y 9 con semilla 42:",
      numero_aleatorio_con_semilla)

# Nota: Si ejecutas este código múltiples veces, obtendrás siempre el mismo número para esta última operación,
# debido a que estamos usando una semilla fija.

print()
print("Nota:")
print("Experimenten cambiando los rangos, las listas y las semillas para ver cómo afecta a los resultados.")
print("Recuerden que los números 'aleatorios' en computación son en realidad pseudoaleatorios y pueden ser reproducidos si se conoce la semilla.")
