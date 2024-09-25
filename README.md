# Este README proporciona instrucciones claras y concisas sobre cómo ejecutar tu aplicación con Docker, además de una breve descripción de la API y sus endpoints.

# API de Chistes de Chuck Norris

Esta es una API REST desarrollada con Django Rest Framework que permite gestionar chistes de Chuck Norris. 
Incluye endpoints para obtener un chiste aleatorio, crear, actualizar y eliminar chistes.

## Requisitos

- Docker
- Docker Compose

## Instrucciones para Ejecutar la Aplicación con Docker

### 1. Clona el Repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd chucknorris_api

2. Construye la Imagen de Docker
Ejecuta el siguiente comando para construir la imagen de Docker:

docker-compose build

3. Ejecuta los Contenedores

docker-compose up

Esto iniciará los servicios definidos en el archivo docker-compose.yml.

4. Accede a la API
La API estará disponible en http://127.0.0.1:8000/api/jokes/

5. Endpoints Disponibles
GET /api/jokes/: Devuelve un chiste aleatorio de la base de datos.
GET /api/jokes/?query=Chuck: Devuelve un chiste aleatorio de la base de datos 'https://api.chucknorris.io/jokes/random'.

POST /api/jokes/create/: Crea un nuevo chiste. Debes enviar un JSON en el cuerpo de la solicitud con el formato:

{
    "joke_text": "Tu chiste aquí"
}

PUT /api/jokes/update/<int:id>/: Actualiza un chiste existente en la base de datos. Debes enviar el nuevo texto del chiste.

DELETE /api/jokes/delete/<int:id>/: Elimina el chiste con el ID especificado.
