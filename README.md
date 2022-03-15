# capitaria
## _Problema base_
Un colegio necesita un sistema para administrar sus cursos. El sistema tiene que soportar que se ingresen varios cursos. Cada curso tendrá un profesor a cargo y una serie de alumnos inscritos. Cada profesor, así como cada alumno puede estar en más de un curso. Además cada curso tendrá una cantidad no determinada de pruebas, y el sistema debe permitir ingresar la nota para cada alumno en cada prueba. Todas las pruebas valen lo mismo.
# Modelo de datos
<img width="893" alt="Captura de Pantalla 2022-03-13 a la(s) 12 01 43" src="https://user-images.githubusercontent.com/95263254/158065865-a054d0d5-5913-4996-9f5a-2cbea6b04ff9.png">

# SQL 

Considerando el enunciado anterior conteste las siguientes preguntas:

- Escriba una Query que entregue la lista de alumnos para el curso "programación"
- Escriba una Query que calcule el promedio de notas de un alumno en un curso.
- Escriba una Query que entregue a los alumnos y el promedio que tiene en cada curso.
- Escriba una Query que lista a todos los alumnos con más de un curso con promedio rojo.
R= se uso sqlite los Query se pueden apreciar en el db browser como se aprecia a continuacion:

<img width="967" alt="Captura de Pantalla 2022-03-15 a la(s) 00 54 04" src="https://user-images.githubusercontent.com/95263254/158302979-48071372-a8e9-4fc4-a533-a7ff30744028.png">
Para hacer un poco mas agradable la visualizacion de esta, utilice jinja para reflejar los datos de la DB en el html, cree algunas tablas con sus datos correspondientes:
<img width="747" alt="Captura de Pantalla 2022-03-15 a la(s) 00 49 02" src="https://user-images.githubusercontent.com/95263254/158302784-dc817da1-2441-4ccf-8142-1f3dc3224753.png">
En la creacion de esta me di cuenta que falto hacer una conexion en cuanto a las notas de las pruebas con los estudiantes, para asi poder realizar el filtro de los alumnos que tengan un minimo de nota 


Dejando de lado el problema del cólegio se tiene una tabla con información de jugadores de tenis: PLAYERS(Nombre, Pais, Ranking). Suponga que Ranking es un número de 1 a 100 que es distinto para cada jugador. Si la tabla en un momento dado tiene solo 20 registros, indique cuantos registros tiene la tabla que resulta de la siguiente consulta:

SELECT c1.Nombre, c2.Nombre

FROM PLAYERS c1, PLAYERS c2

WHERE c1.Ranking > c2.Ranking

Seleccione las respuestas correctas:

a) 400

b) 190

c) 20

d) imposible saberlo
R= D

# Diseño de software 
## Backend

Si usted estuviera resolviendo el problema del colegio implementando una aplicación web que incluya las siguientes funcionalidades:

- CRUD alumnos, cursos, pruebas y notas.
- Listar a los alumnos junto a su promedio de notas.
- Filtar a todos los alumnos con más de un ramo con promedio rojo.

El CRUD lo lleve a cabo con ipython 
<img width="1200" alt="Captura de Pantalla 2022-03-15 a la(s) 01 00 29" src="https://user-images.githubusercontent.com/95263254/158303740-cc227ea5-3baa-4803-8abb-2d8cc71fe7b8.png">
El for que se intento hacer en shell esta en el html donde se uso jinja para mostrar ese valor buscado que era el nombre del curso 
Fue algunos de los Crud que pude realizar por el detalle que se reflejo al princio cuando se hablo de los Query, de igual manera si se tuviera la conexion adecuada para realizar un filtro de todos los alumnos con mas de un ramo rojo seria de la siguiente manera:
```sh
Estudiante.objects.filter(ramo=3.9)
```
## Frontend
Construya una función o clase en JS que recibiendo el siguiente JSON por parámetro, permita renderear una agenda semanal en html y con bloques de 30 minutos:
Unicamente frontend de una agenda (sin JSON)
<img width="962" alt="Captura de Pantalla 2022-03-13 a la(s) 21 33 22" src="https://user-images.githubusercontent.com/95263254/158086550-cd45f536-ff78-41b0-872b-786e5b00ce6e.png">
Agenda con JSON (falta agregar las casillas tomadas)
<img width="1022" alt="Captura de Pantalla 2022-03-13 a la(s) 23 48 56" src="httpsEXTRA://user-images.githubusercontent.com/95263254/158096440-1345077d-158f-4a1b-a253-948a2326a4f5.png">

## PIP INSTALL (en mac pip3 install)

Install JINJA (se puede con pip o con easy_install)
```sh
easy_install Jinja2
pip install jinja2 
```
Install django
```sh
python -m pip install Django (linux/mac)
py -m pip install Django
```
Extra (ipython para el shell)
```sh
pip3 install ipython
``` 
