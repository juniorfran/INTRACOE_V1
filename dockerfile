# Cambiar a Python 3.10-slim-bullseye (o Python 3.11)
FROM python:3.10-slim-bullseye
# O usa FROM python:3.11-slim-bullseye para Python 3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los requisitos del archivo requirements.txt
COPY requirements.txt .

# Instalar las dependencias necesarias para mysqlclient y pkg-config
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc pkg-config libmariadb-dev python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar los requisitos de Python
RUN pip install --upgrade pip setuptools && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación en el contenedor
COPY . .

# Ejecutar el comando collectstatic durante la construcción
#RUN python3 manage.py collectstatic --noinput

# Exponer el puerto en el que la aplicación estará corriendo
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
