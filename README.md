# Web-Scraping

## ***Descripción del proyecto***

Como consecuencia de la pandemia, los dos miembros de este equipo coincidimos en nuestras ganas de poder volver a viajar de nuevo. Por ello, y buscando una idea que podamos reutilizar en el futuro, nos hemos propuesto enfocar esta práctica en la obtención de los mejores resultados de alquileres turísticos en distintas zonas, con el fin de poder conseguir buenos tratos en cuanto por fin, podamos salir de viaje. 

Concretamente vamos a analizar y scrapear la web de alquileres https://www.hometogo.com, por tratarse de un agregador de alquileres con información de airbnb, booking, entre muchas otras... Como suele decirse, quien scrapea a un scrapeador, tiene 100 años de perdón; así que esperamos que este proyecto sea de mucha utilidad (sobre todo, porque ello significará que la pandemia nos da un respiro!)

Un buen viajero no tiene planes fijos ni tampoco la intención de llegar, pero es necesario un lugar donde dormir!

## ***Procedimiento***

### User Experience ###

Lo primero que miramos es la experiencia de usuario al entrar en https://www.hometogo.com. 
![](.README_images/pag principal suiza.png) para tener claro qué queremos extraer y cómo.
Como usuario, cuando entro en hometogo, lo primero que hago es seleccionar:
- Destino
- Fechas
- Nº de personas
- Le damos a search

Al hacer la búsqueda nos aparece un listado de resultados:
#FALTA IMAGEN
con información de cada uno de los alojamientos disponibles.
Adicionalmente si clicamos en "DETALLES" se nos redirige a una página donde nos da todos los detalles del alojamiento:
![](.README_images/detalles.png)

Una vez tenemos clara la experiencia de usuario que queremos replicar con el web scraping podemos pasar a definir cuál es el process map que mejor representa dicha experiencia.

### Process Map ###
![](.README_images/Lucidchart.png)

En este proyecto nos quedaremos solo con los resultados de la primera página ya que en una única página hay aproximadamente 280 resultados, y son suficientes para el trabajo que queremos hacer.

### Inspeccionar elementos de la página de resultados ###
#### ¿Cuál es la información que nos interesa extrear? ####

1) Nombre del alojamiento
2) Donde encontrar el alojamiento
3) Especificaciones del alojamiento
4) Precio total del alojamiento
5) Localización del alojamiento
6) Política de cancelación
7) Link a más detalles

![](.README_images/Inspeccion.png)