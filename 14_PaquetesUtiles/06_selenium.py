# =================================================================
# AUTOMATIZACIÓN DE NAVEGADOR WEB CON SELENIUM
# =================================================================
"""
Este script demuestra cómo usar Selenium para automatizar interacciones
con un navegador web, específicamente para realizar un inicio de sesión
en GitHub de forma automática y segura.

Requisitos de instalación:
-------------------------
1. No nombrar el archivo como selenium.py para evitar conflictos
2. Instalar Selenium: pipenv install selenium
3. Instalar python-dotenv: pipenv install python-dotenv

Conceptos importantes:
---------------------
- Selenium: Framework para automatización de navegadores web
- WebDriver: Interface para controlar el navegador
- Locators: Métodos para encontrar elementos en la página web
- Waits: Mecanismos para esperar que elementos estén disponibles
"""

# =================================================================
# SECCIÓN 1: IMPORTACIONES Y CONFIGURACIÓN INICIAL
# =================================================================

# Importaciones principales de Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By  # Para localizar elementos
from selenium.webdriver.support.ui import WebDriverWait  # Para esperas explícitas
from selenium.webdriver.common.keys import Keys  # Para simular teclas
from selenium.webdriver.support import expected_conditions as EC  # Condiciones de espera

# Importaciones para manejo de variables de entorno
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# =================================================================
# SECCIÓN 2: CONFIGURACIÓN DEL NAVEGADOR
# =================================================================

# Ejemplo básico de inicio de Chrome (comentado)
"""
# Versión simple de inicio del navegador
browser = webdriver.Chrome()
browser.get("https://www.google.com")   # Abrir una página web en Chrome

# Salida esperada:
PS C:\PythonCourse> & C:/Users/econo/.virtualenvs/14_PaquetesUtiles-vVT4Ex2a/Scripts/python.exe c:/PythonCourse/14_PaquetesUtiles/06_selenium.py
DevTools listening on ws://127.0.0.1:65424/devtools/browser/d5a4e990-c020-4392-b098-7a9e4b8a9d24

# Cerrar el navegador
browser.quit()
"""

# Configuración avanzada del navegador
options = webdriver.ChromeOptions()
# Mantener el navegador abierto
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

# Configurar tiempo de espera implícito global
# Esperar hasta 10 segundos cuando busque elementos
browser.implicitly_wait(10)

# =================================================================
# SECCIÓN 3: NAVEGACIÓN Y LOGIN EN GITHUB
# =================================================================

# Navegar a GitHub
browser.get("https://www.github.com")

# Encontrar y hacer clic en el enlace de inicio de sesión
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

# Nota: Al ejecutar este código, GitHub detectará que se está usando
# software automatizado de pruebas controlando Chrome

# =================================================================
# SECCIÓN 4: INTERACCIÓN CON FORMULARIO DE LOGIN
# =================================================================

# Localizar elementos del formulario usando sus IDs
user_input = browser.find_element(By.ID, "login_field")
password_input = browser.find_element(By.ID, "password")

# Ingresar credenciales desde variables de entorno
user_input.send_keys(os.environ.get("gh_user"))
password_input.send_keys(os.environ.get("gh_password"))
password_input.send_keys(Keys.RETURN)  # Simular presionar Enter

"""
NOTA IMPORTANTE SOBRE SEGURIDAD:
-------------------------------
1. Las credenciales se almacenan en un archivo .env:
   gh_user=usuario
   gh_pass=contraseña
   
2. El archivo .env NUNCA debe subirse a GitHub
3. Agregar .env al archivo .gitignore
4. Usar python-dotenv para leer las variables de entorno
"""

# =================================================================
# SECCIÓN 5: VERIFICACIÓN DE LOGIN EXITOSO
# =================================================================

# Ejemplo comentado de verificación simple
"""
profile_link = browser.find_element(
    By.CLASS_NAME,
    "Truncate__StyledTruncate"
)
label = profile_link.get_attribute("innerHTML")
print(label)
"""

# Verificación robusta con manejo de errores y esperas explícitas
try:
    # Crear un objeto de espera explícita
    wait = WebDriverWait(browser, 10)

    # Esperar y buscar elemento que confirme login exitoso
    user_element = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".user-mention[href$='/adalovelace-ec']"))
    )
    print(f"¡Login exitoso! Usuario conectado: {user_element.text}")
except Exception as e:
    print("No se pudo verificar el usuario")
    print("URL actual:", browser.current_url)

# =================================================================
# SECCIÓN 6: LIMPIEZA (comentado para mantener navegador abierto)
# =================================================================

# Cerrar el navegador cuando sea necesario
# browser.quit()
