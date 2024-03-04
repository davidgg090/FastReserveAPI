# Sistema de Reservaciones para Restaurante con FastAPI

Este proyecto es un sistema de reservaciones para restaurantes implementado con FastAPI, diseñado para demostrar la creación de APIs RESTful utilizando este moderno y rápido framework para Python. Permite a los usuarios crear, leer, actualizar y eliminar reservaciones, así como gestionar usuarios y mesas en el restaurante.

## Características

- CRUD de reservaciones.
- CRUD de usuarios.
- CRUD de mesas.
- Autenticación y autorización con JWT.
- Filtrado y paginación de reservaciones.

## Tecnologías Utilizadas

- FastAPI
- SQLAlchemy para ORM.
- Pydantic para la validación de datos.
- PostgreSQL como sistema de gestión de base de datos.
- JWT para la autenticación.

## Instalación

1. Clona este repositorio:
    
    ```
    git clone
    ```

2. Instala las dependencias:
    
    ```
    cd fastapi-restaurant-reservation
    pip install -r requirements.txt
    ```

3. Configura tu archivo `.env` con las variables de entorno necesarias (ver `example.env` para un ejemplo).

4. Ejecuta el servidor:
        
     ```
        uvicorn app.main:app --reload
     ```
   

## Uso

Una vez que el servidor está en ejecución, puedes acceder a la documentación interactiva de la API en `http://127.0.0.1:8000/docs` para ver todos los endpoints disponibles y probarlos directamente desde tu navegador.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, siente libre de fork el repositorio y enviar tus pull requests.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
