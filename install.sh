#!/bin/bash

# Verificar si se está ejecutando con source
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "[!] Debes ejecutar este script usando 'source' o '.' para mantener el entorno virtual activo."
    echo "Ejemplo: source install.sh o . install.sh"
    exit 1
fi

# Instalar python3-venv si no está instalado
if ! dpkg -l | grep -q python3-venv; then
    echo "[+] El paquete python3-venv no está instalado. Instalándolo..."
    sudo apt update
    sudo apt install -y python3-venv

    if [ $? -ne 0 ]; then
        echo "[!] Error al instalar python3-venv. Asegúrate de tener permisos sudo."
        exit 1
    fi
else
    echo "[+] python3-venv ya está instalado."
fi

# Crear el entorno virtual
echo "[+] Creando el entorno virtual..."
python3 -m venv myenv

if [ $? -ne 0 ]; then
    echo "[!] Error al crear el entorno virtual."
    exit 1
fi

echo "[+] Entorno virtual creado."

# Activar el entorno virtual
echo "[+] Activando el entorno virtual..."
source myenv/bin/activate

if [ $? -ne 0 ]; then
    echo "[!] Error al activar el entorno virtual."
    exit 1
fi

# Instalar selenium dentro del entorno virtual
echo "[+] Instalando Selenium en el entorno virtual..."
pip install selenium

if [ $? -ne 0 ]; then
    echo "[!] Error al instalar Selenium. Verifica que todo esté correctamente configurado."
    exit 1
fi

echo "[+] Selenium y dependencias instaladas correctamente."
echo "[+] El entorno virtual se ha activado y está listo para usar."
echo "[+] Puedes ejecutar tus scripts Python ahora sin problemas."
