Hola Mundo

# Entorno virtual

Con el siguiente comando:

```bash
virtualenv venv
```

Se genera una carpeta llamada `venv`, la cual contiene diversos archivos que nos permitarán activar/desactivar nuestro entorno.

Desde la raíz del proyecto puedo activar el entorno.

Desde Windows con Powershell:

```bash
.\venv\Scripts\activate
```

```python
def main():
    print(7)
```

Desde terminal Gitbash y UNIX (linux y macOS):
```bash
source env/Scripts/activate
```
# Configuracion inicial
## Configuracion del archivo .env
Creacion del archivo **.env**, para configurar variables de entorno, contiene:
```python
FLASK_APP=app.py #indica cual es el archivo principal, 
FLASK_DEBUB=1   #modo de depuracion
FLASK_RUN_PORT=5050 #configurar puerto
FLASK_RUN_HOST=127.0.0.1 #Para acceder en red
```
Otras funciones adicionales, para configurar la url del servicio:
```python
FLASK_RUN_HOST=0.0.0.0 #Para acceder en red local desde cualquier dispositivo dentro de la red, incluso desde un celular
```
Si el archivo principal esta dentro de una **carpeta**, agregar
```python
FLASK_APP=nomcarpeta.app.py #indica cual es el archivo principal, 
```
Adicionalmente, en la carpeta agregar un archivo llamado
```python
__init__.py
```
# Instalación de dependencias

Usualmente se usa el archivo requirements.txt, em el cual especificamos las dependencias que usaremos en nuestro proyecto.

```bash
pip install -r requirements.txt
```

Puede ser otro nombre de archivo también

## Verificando dependencias instaladas

```bash
pip freeze
```


Una vez instalada las librerias se puede hacer uso de ellas como 
```bash
from flask import Flask 
```

Luego para levantar el servicio web del proyecto
usar el siguiente comando:
```bash
flask run
```

