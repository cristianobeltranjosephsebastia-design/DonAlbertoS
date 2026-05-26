#!/bin/bash

echo "Iniciando el despliegue automatico de Don Alberto"

# Moverse a la carpeta

cd /home/$USER/moto-api

# Traer los cambios desde git

echo "Trayendo la ultima version desde git"

git pull origin master
source venv/bin/activate
pip install -r requeriments.txt --quiet

# Reiniciar el servicio de systemd

echo "Reiniciando el motor gunicorn"
sudo systemctl restart flask_app.service

# Verificar que este vivo
echo "Despliegue completado con exito. El estado actual es:"
sudo systemctl status flask_app.service | grep "Active:"
