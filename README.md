# Selenium CAPTCHA Bypass Script

Es una herramienta que automatiza la soluciòn de captchas para realizar fuerza bruta a páginas de incio de sesiòn protegidas por captchas. Se resuelve el catpcha de sitios web protegidos con reCAPTCHA, para lo cual se usa **Selenium** y la extensión **noCaptcha**. La herramienta resuelve los captchas de forma automática. Es ideal para fines educativos y de investigación en entornos controlados para poder ejecutar ataques de fuerza bruta y bypassear el control del captcha ya que el mismo se automatiza con este bot.

![silentCaptcha](https://github.com/user-attachments/assets/79502eb7-6e91-4279-a351-220646bcfec4)


## Características

- Automatización del ingreso de credenciales en sitios web con CAPTCHA.
- Uso de Selenium para la interacción con el navegador.
- Bypass de reCAPTCHA utilizando la extensión noCaptcha.

## Requisitos

Antes de ejecutar el script, asegúrate de cumplir con los siguientes requisitos:

- **Python**: Versión 3.12.6 o superior.
- **Geckodriver**: Driver necesario para controlar Firefox con Selenium.
- **Selenium**: Librería para la automatización de navegadores web.
- **Extensión noCaptcha**: Extensión utilizada para el bypass de CAPTCHA.

## Instalación

Sigue los pasos a continuación para instalar las dependencias y configurar el entorno.

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/sk8ware/Revers3Everything.git
cd Revers3Everything
```

### 2. Instalar dependencias

Ejecuta el script `Install.sh` para instalar automáticamente todas las dependencias necesarias, activar el entorno virtual, e instalar Selenium:

```bash
source Install.sh
```

Este script:
- Instalará `python3-venv` si no está presente.
- Creará y activará un entorno virtual.
- Instalará `selenium` dentro del entorno virtual.
- Verificará la instalación de **Geckodriver**.

### 3. Ejecutar el script

Una vez que el entorno esté configurado, ejecuta el script `NoCaptcha.py` con los parámetros necesarios:

```bash
python3 NoCaptcha.py https://web-con-Captcha/ usuarios.txt contraseñas.txt
```

- **URL del sitio web con CAPTCHA**: El primer argumento es la URL del sitio web donde deseas intentar el bypass.
- **Archivo de usuarios**: El segundo argumento es el archivo que contiene una lista de nombres de usuario.
- **Archivo de contraseñas**: El tercer argumento es el archivo que contiene una lista de contraseñas.

## Notas importantes

- **Uso educativo**: Este script está destinado para fines educativos y de investigación en entornos controlados. No debe ser utilizado en sitios web donde no tengas permiso explícito para realizar pruebas.
- **Actualizaciones**: Asegúrate de tener las versiones más recientes de **Selenium** y **Geckodriver** para evitar errores de compatibilidad.

## Contribuciones

Si tienes sugerencias o mejoras, no dudes en abrir un _pull request_ o crear un _issue_ en este repositorio.
