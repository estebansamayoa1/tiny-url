
![lmm](img/logo.png)


## Intro
Haremos un creador de tiny url (URL shortener), aplicaremos conceptos de CS como:

- REST APIs
- Web development
- key-val databases, [Redis](https://redis.io/topics/introduction)
- HTTP verbs
- HTTP responses

> usara la libreria [redis](https://pypi.org/project/redis/) para trabajar

---
## App

La aplicacion se vera asi:


![1](img/mock1.png)

La app tendra por lo menos 3 vistas (3 rutas):

1. [`/`](/tiny-urls) : Crear tinyURL
2. [`/urls`](/url-list): lista de URLs
3. [`/stats`](/stats): estadistica de clicks y visitas

---

# Nota
Es importante que su aplicacion tenga un dominio, casi en todos los proyectos hemos trabajado con `127.0.0.1:5000` pero ese no es un dominio real, para usar un nombre de dominio hay varias maneras, gratis

- [/etc/hosts](https://support.acquia.com/hc/en-us/articles/360004175973-Using-an-etc-hosts-file-for-custom-domains-during-development#:~:text=The%20%2Fetc%2Fhosts%20file%20contains,before%20making%20a%20website%20live.)
- [nip.io](https://nip.io/) [Recomendado]
- se puede no usar dominio y seguir usando `127.0.0.1:5000`

> se puede obtener dinamicamente el HOST url con el [Host Header](https://stackoverflow.com/questions/43156023/what-is-http-host-header)

---

