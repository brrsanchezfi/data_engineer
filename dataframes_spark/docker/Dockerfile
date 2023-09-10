FROM alpine:latest

# Instala las dependencias necesarias
RUN apk update && apk add --no-cache python3 py3-pip openjdk8-jre

# Configura variables de entorno
ENV SPARK_HOME=/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Descarga Spark
RUN wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz -O /tmp/spark.tgz && \
    tar xzf /tmp/spark.tgz -C / && \
    rm /tmp/spark.tgz && \
    mv /spark-3.1.2-bin-hadoop3.2 /spark

# Copia spark-env.sh
COPY docker/spark-env.sh $SPARK_HOME/conf/spark-env.sh

# Instala las dependencias de Python
COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

WORKDIR /app

CMD ["/bin/sh"]
