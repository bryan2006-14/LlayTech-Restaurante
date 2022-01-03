# iCard (_Backend_)

## *React y Django: Crea una carta digital para restaurantes*

_Backend_ para la aplicación **iCard** creado con _Django REST Framework_.

Funciones principales:
+ Gestión de usuarios (_CRUD_)
+ Autenticación (_Token_)
+ Gestión de categorías (_CRUD_)

Incluye:
+ **Django REST Framework**
+ Entorno virtual con **venv**
+ Documentación de la API con **drf-yasg**
+ Autenticación con **JWT**

### Librerías y paquetes utilizados:
- [**Django REST framework**](https://www.django-rest-framework.org/)
- [**drf-yasg**](https://drf-yasg.readthedocs.io/en/stable/)
- [**Simple JWT**](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [**Django CORS Headers**](https://pypi.org/project/django-cors-headers/)
- [**Pillow**](https://pypi.org/project/Pillow/)

### Versión: 1.0.0

### Notas:
Comando para activar el entorno virtual:
```
./envs/icard/Scripts/activate
```

Comando para instalar las dependencias del proyecto desde el fichero requirements.txt (con el entorno virtual activado):
```
pip install -r requirements.txt
```

Comando para crear o actualizar el fichero requirements.txt (con el entorno virtual activado):
```
pip freeze > requirements.txt
```

Comando para ejecutar el servidor en desarrollo:
```
python manage.py runserver
```
