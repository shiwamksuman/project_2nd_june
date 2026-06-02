from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from error_handling.config.ConfigStore import *
from error_handling.functions import *

def malformed(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("account_id", StringType(), True), StructField("company_name", StringType(), True), StructField("industry", StringType(), True), StructField("region", StringType(), True), StructField("country", StringType(), True), StructField("annual_revenue", StringType(), True), StructField("employee_count", StringType(), True), StructField("tier", StringType(), True), StructField("created_date", StringType(), True), StructField("_corrupt_record", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .option("columnNameOfCorruptRecord", "_corrupt_record")\
        .csv("dbfs:/Volumes/main/prophecy_lh/malformed/malformed_records.csv")
