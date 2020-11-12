# Extras


Estas son algunas sugerencias de puntos extra:

- una vista de `/admin` en donde se pueda administrar la base de datos completa, se puede hacer flush all de todas las URLs etc.

- una vista de `/load` en donde se cargue un csv (tinyURL,originalURL) y se inserte el contenido a la DB.

- una vista de `/search` en donde se puede buscar alguna URL en especifico.

- hacer registro de la hora en la que se creo el entry y tambien mostrar eso en las vistas de `/stats` & `/urls`

- hacer registro usando dicts, key: hashID y value: {"url": "long-url.com"} [info aqui](https://stackoverflow.com/questions/32276493/how-to-store-and-retrieve-a-dictionary-with-redis)
