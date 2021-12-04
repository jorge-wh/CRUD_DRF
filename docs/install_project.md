# Pasos para la instalacion | CRUD DRF

## Descargar el Proyecto

_1.1_ Nos posicionamos en /var/waps/sitios

    cd /var/waps/sitios

_1.2_ Clonar el proyecto

    git@github.com:jorge-wh/CRUD_DRF.git

## Crear entorno

_1.1_ Nos posicionamos en /var/waps/entornos

    cd /var/waps/entornos

_1.2_ Crear el entorno

    python3 -m venv test_api

_1.3_ Activar el entorno

    workon test_api

    Si falla:
    source bin/activate

## Instalar Requerimientos

_1.1_ Nos posicionamos en el proyecto /var/waps/sitios/CRUD_DRF

    cd /var/waps/sitios/CRUD_DRF

_1.2_ Aplicar pip install

    pip3 install -r requirements.txt
