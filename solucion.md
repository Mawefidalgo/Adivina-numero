## Iniciamos el proyecto AdivinaNumero:
```bash
django-admin.exe startproject AdivinaNumero .
```
## En el fichero AdivinaNumero/setting.py configuramos los ajustes:
## El lenguaje del codigo
```python
LANGUAGE_CODE = 'es-es'
```
## La zona horaria
```python
TIME_ZONE = 'Europe/Berlin'
```
## Añadimos lo siguiente debajo de ESTATIC_ROOT
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```
## Modificamos los puertos
```python
ALLOWED_HOSTS = ['localhost','127.0.0.1']
```

## Antes de iniciar el servidor creamos una base de datos para Adivina Numero:
```bash
 python manage.py migrate
```

## Ahora si podemos iniciar el servidor:
```bash
python manage.py runserver
```
