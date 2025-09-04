FROM jupyter/pyspark-notebook:python-3.11

# Cambiamos a root para poder escribir en /usr/local/spark/jars
USER root
ENV DEBIAN_FRONTEND=noninteractive

# Aseguramos que exista la carpeta y tengamos permisos
RUN mkdir -p /usr/local/spark/jars && chown -R ${NB_UID}:${NB_GID} /usr/local/spark

# Descargamos los JARs necesarios para s3a (Spark -> S3/MinIO)
# Nota: curl ya viene en la imagen base; si no, apt-get update && apt-get install -y curl
RUN curl -L -o /usr/local/spark/jars/hadoop-aws-3.3.4.jar https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    curl -L -o /usr/local/spark/jars/aws-java-sdk-bundle-1.12.262.jar https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

# Volvemos al usuario jovyan (no root)
USER ${NB_UID}

# Requisitos Python
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/jovyan/work
