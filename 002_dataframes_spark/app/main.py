from pyspark.sql import SparkSession

# Inicializa SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

# Carga los datos desde un archivo CSV
df = spark.read.csv("..\dataframes_spark\data\Horse Racing Results.CSV", header=True, inferSchema=True)

# Realiza operaciones con DataFrames
# ...

# Detén la sesión de Spark
spark.stop()
