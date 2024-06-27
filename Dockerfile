# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación Flask
EXPOSE 80

# Define el comando de ejecución de la aplicación con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "getSolve:app"]
