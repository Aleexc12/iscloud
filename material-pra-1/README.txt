============================= Estructura =============================

Estructura de esta carpeta:
 - README.txt: este documento
 - game-store: servicio REST
 - swagger: Swagger UI con descripción de la API
 - init-db.sql: Fichero de inicialización de la base de datos

============================= Base de datos =============================

El servicio es compatible con ProstgreSQL, y se ha probado en su versión 15.

Para configurar el acceso a la base de datos, se puede utilizar una variable
de entorno, DATABASE_URI, con el siguiente formato:

postgresql://{db_user}:{db_password}@{db_host}/{db_name}

Por defecto, se utiliza la siguiente URI en el caso de que no se proporcione
una: 

postgresql://aws:flaskroot@localhost/practica

Se proporciona un fichero, init-db.sql, que crea una base de datos con nombre
práctica, así como un usuario con nombre 'aws' y contraseña 'flaskroot', con 
acceso a dicha base de datos.

============================= API REST =============================

La API REST está escrita en Python, usando Flask, y requiere de ciertas
dependencias, que están definidas en el fichero requirements.txt.

Se debe utilizar 'pip' para instalar dichas dependencias.

con el mandato 'python3 initAlchemy.py' se podrá iniciar un servidor de pruebas
del servicio, pero se requerirá de un software wsgi para ejecutar el servicio 
en EC2 en modo daemon, como, por ejemplo, gunicorn. 'gunicorn --bind 0.0.0.0:5000 initAlchemy:api --daemon' 

============================= Swagger =============================

En la carpeta swagger se ofrece un Swagger UI, ya configurado, con la definición
de la API.

El fichero 'swagger-config.yaml' es el que incluye la definición de la API.

Debéis modificar la URL de acceso al servicio en dicho fichero, para que apunte
a vuestro servicio en AWS, para poder hacer pruebas.
