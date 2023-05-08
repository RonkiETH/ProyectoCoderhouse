
# Proyecto Python Coderhouse

## Deploy

Para iniciar este proyecto:

**Creá un entorno virtual:**
```bash
py -m venv venv
```

**Activá el Entorno Virtual:**
```bash
Presioná F1
Seleccionar Interprete
.\venv\Scripts\activate
```

**Instalá Django**
```bash
pip install django
```

**Instalá Dotenv**
```bash
pip install python-dotenv
```

**Configura tu SECRET_KEY**
```bash
En manage.py vas a agregar este código:
from dotenv import load_dotenv
load_dotenv()

Creá un archivo .env 
En el archivo .env vas a agregar lo siguiente:
SECRET_KEY = 'TU_CLAVE'

En el archivo settings.py:
import OS
Y en el valor de SECRET_KEY vas a poner lo siguiente:
SECRET_KEY = os.environ.get('SECRET_KEY')
```
**Realiza las migraciones necesarias**
```bash
python manage.py migrate
```

**Iniciá el proyecto**
```bash
python manage.py runserver
```

## Adicional
**Creá un superusuario (Para ver la consola de admnistrador)**

#Crear un superusuario
```bash
python manage.py createsuperuser
``` 
