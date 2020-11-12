
## Tiny URLs

### Modo Normal
En esta vista se podra generar un tinyURL, el usuario ingresa una URL cualquiera (www.google.com por ejemplo) apachara el boton magico y su app debera hacer lo siguiente:

1. Recibir la URL
2. Generar un ["token/identificador" unico](https://pypi.org/project/shortuuid/) (ejemplo: cyu3tzA)
3. Guardar ese token en la base de datos (key-val) donde el "token" sera el key y la URL sera el val
4. Debera responder con la tinyURL generada al usuario.


> el generador puede ser una funcion de SU AUTORIA.

### Modo Custom

En esta modalidad sucedera todo lo anterior con la excepcion del paso "2" en donde el usuario ademas del URL tambien podra ingresar un customID (palabra unica que identifique a su URL)

```bash
Ejemplo:

URL: www.google.com
customID: mi-url

Resultado => http://su-dominio.com/mi-url

```
Al resultado puede agregarle un [boton de "copy"](https://www.w3schools.com/howto/howto_js_copy_clipboard.asp)


Mockup:

![1](img/mock1.png)

### Funcionamiento

Cuando el usuario pegue en su browser, obviamente su aplicacion respondera y recibira este request debera [REDIRECT](https://moz.com/learn/seo/redirection) al usuario a la URL original.


Esto quiere decir que su app debe responder con el "response code" CORRECTO!.

```
Ejemplo:

Browser: http://su-dominio.com/mi-url

App: recibe [http://su-dominio.com/mi-url]

Browser: [redirect] www.google.com
```

## Ejemplos:

- [https://tinyurl.com/](https://tinyurl.com/)
- [https://tiny.cc/](https://tiny.cc/)

---

> Creame todo lo vimos en clase.
