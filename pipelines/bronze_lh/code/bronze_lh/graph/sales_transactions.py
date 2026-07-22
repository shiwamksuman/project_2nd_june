from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *

def sales_transactions(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", StringType(), True), StructField("customer_id", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", StringType(), True), StructField("category", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/data/sales_transactions.csv")
