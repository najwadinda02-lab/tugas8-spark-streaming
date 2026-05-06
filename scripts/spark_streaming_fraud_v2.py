from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os

# Inisialisasi Spark Session
spark = SparkSession.builder \
    .appName("Fraud Detection Najwa") \
    .getOrCreate()

# Set log level ke ERROR agar console tidak penuh dengan pesan INFO
spark.sparkContext.setLogLevel("ERROR")

# 1. Membaca Data dari Kafka
df_kafka = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank_topic") \
    .option("startingOffsets", "latest") \
    .load()

# 2. Definisi Schema JSON
schema = StructType([
    StructField("nama", StringType()),
    StructField("rekening", StringType()),
    StructField("jumlah", IntegerType()),
    StructField("lokasi", StringType())
])

# 3. Parsing Data JSON
df = df_kafka.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# 4. Masking & Fraud Detection Logic
# Masking: menyembunyikan nomor rekening (contoh: ****82)
# Fraud: Jika jumlah > 50jt ATAU lokasi di Luar Negeri
df_final = df.withColumn("rekening_masked", concat(lit("****"), col("rekening").substr(-2, 2))) \
             .withColumn("status", when(col("jumlah") > 50000000, "FRAUD")
                                  .when(col("lokasi") == "Luar Negeri", "FRAUD")
                                  .otherwise("NORMAL"))

# 5. Menulis Output ke Parquet
# Pastikan path ini sesuai dengan struktur folder di terminalmu
query = df_final.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option("path", "stream_data/realtime_output/") \
    .option("checkpointLocation", "data/checkpoints/fraud_detection_query") \
    .start()

print("Streaming sedang berjalan... Menunggu data dari Kafka.")

# Menjaga agar script tetap running
query.awaitTermination()