# Imagen base de Python
FROM python:3.11.10-slim

# Crear directorio principal en el contenedor
WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY game-store/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copiar solo el código fuente necesario de la aplicación
COPY game-store/ /app/game-store/

# Exponer el puerto en el que se va a ejecutar
EXPOSE 5000

# Configurar la variable de entorno para Flask
ENV FLASK_APP=game-store/util/apiAlchemy.py

# Comando para ejecutar la aplicación
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


