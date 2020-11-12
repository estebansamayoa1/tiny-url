
# URLS
En esta vista se mostraran todas las URLs convertidas hasta el momento, sera mostrado en una tabla a 2 columnas

| tinyURL                       	|                Original URL                	|
|-------------------------------	|:------------------------------------------|
| http://mi-dominio.com/sasd3av 	| https://miu.ufm.edu/mis_cursos_detalle.php 	|
| http://mi-dominio.com/1wsqzdf 	| https://docs.google.com/document/d/1       	|
| http://mi-dominio.com/correo  	| https://mail.google.com/mail/u/            	|

Esto se obtiene yendo a la base de datos (Redis) recorrer los keys,vals y renderizar esos resultados.


La ultima opcion es que el usuario podra borrar una URL especifica con un boton o como ud prefiera; En un web app la manera correcta para borrar un recurso es usando el verbo [DELETE](https://restfulapi.net/http-methods/#delete); Al elegir borrar la URL debera de ir a la base de datos y borrar el entry.


> el mockup para esta funcion seria este:

![1](img/urls.png)


# Extra

Si gusta puede implementar un metodo "search" que con un search-box le permita al usuario hacer un busqueda de las URLS o tiny URLs.
