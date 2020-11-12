
# Run

Su aplicacion debe correr 100% en docker y docker-compose, instalar redis en su OS no es una opcion.

Yo le proveo con un scratch project donde ya tengo configurado redis y la app.

Basta con correr

`docker-compose up --build`

eso corre:
- app sencilla de python
- redis
- app conectada a redis



```bash
# DEBE CORRER USANDO DOCKER
# example 1
docker run -it -p 8080:8080 your-image/love-my-movies:1.20

# example 2
docker-compose up

```
