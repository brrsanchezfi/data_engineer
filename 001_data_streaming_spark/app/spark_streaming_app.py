from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Configura el contexto de Spark
sc = SparkContext("local[2]", "SparkStreamingExample")
ssc = StreamingContext(sc, 1)  # Intervalo de procesamiento: 1 segundo


from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


spark = SparkSession.builder \
    .appName("SparkStreamingApp") \
    .getOrCreate()


schema = StructType([
    StructField("timestamp", StringType(), True),
    StructField("value", IntegerType(), True)
])


raw_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "mi_topic") \


