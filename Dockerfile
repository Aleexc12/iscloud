#Imagen base de python
FROM python:3.11.10-slim
#Crear directorio principal en el contenedor
WORKDIR /app
#Copiar requirements.txt para instalar todas las librerías de python necesarias
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#Copiar el código fuente de la aplicación #Siempre poner más tarde los ficheros que puede q cambies
COPY app.py app.py 
#Exponemos el puerto en el que se va a ejecutar
EXPOSE 5000
#Indicamos el comando que tiene que ejecutar el contenedor
CMD ["python3" ,"-m", "flask", "run", "--host=0.0.0.0"]