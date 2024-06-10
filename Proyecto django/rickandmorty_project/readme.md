# Proyecto de Aplicación Django utilizando la API de Rick and Morty

Este proyecto consiste en una aplicación web desarrollada con Django que consulta la API pública de Rick and Morty para mostrar datos relevantes de la serie animada. Los datos obtenidos se muestran en una tabla HTML dentro de una página web generada por Django.

## API de Rick and Morty

La API de Rick and Morty es una API pública que proporciona información sobre la serie de televisión animada "Rick and Morty". Proporciona acceso a datos sobre personajes, episodios y ubicaciones de la serie.

Para este proyecto, estamos consultando principalmente datos sobre personajes, como nombres, especies, género, estado, etc.

La documentación oficial de la API se puede encontrar en: [Rick and Morty API Documentation](https://rickandmortyapi.com/documentation)

## Interacción con la API en la Aplicación Django

En la aplicación Django, hemos creado una vista utilizando Django views que hace una solicitud a la API de Rick and Morty para recuperar datos sobre los personajes de la serie.

Hemos utilizado el módulo `requests` de Python para realizar solicitudes HTTP a la API y obtener los datos en formato JSON.

Después de recibir los datos, los procesamos según sea necesario y los pasamos a una plantilla HTML utilizando el sistema de plantillas de Django para renderizarlos en una tabla HTML.

