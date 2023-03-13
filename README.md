<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Cli Guadalupe Data

## `paco_el_chato`
Paco el chato es el asistente para las tareas de gabinete en el proyecto de erradicación de gato
feral en Isla Guadalupe.

Tiene tres habilidades:
- clasificar fotos con gatos
- generar un esbozo del mapa con trampas activas y desactivas de Isla Guadalupe
- Actualizar la paquetería para hacr las tareas anteriores

## `haz-mapa`
Hace un esbozo del mapa de Isla Guadalupe con las trampas activas e inactivas.
**Requerimiento**: En la carpeta de trabajo debe estar:
- IG_POSICION_{fecha}.txt         : Archivo que obtenemos de mapsource
- IG_POSICION_TRAMPAS_{fecha}.xlsx: Archivos con los esfuerzos de la semana
Al final generará el archivo `map_of_traps.jpg`.

## `clasifica-fotos`
Clasifica las fotos que vienen de las trampas cámara. \n
**Requerimiento**: En la carpeta de trabajo debe estar una carpeta (varias carpetas) con las fotos.
El nombre de la carpeta principan debe ser sin espacios. Por ejemplo: \n
- `FOTOS GATOS`: es un nombre incorrecto, \n
- `FOTOS_GATOS`: es un nombre correcto. \n
Al final generará una carpeta con las fotos en las que detectó gato.

## `actualiza-comandos`
Actualiza los comandos:
- `haz-mapa`
- `clasifica-fotos`
