from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from error_handling.config.ConfigStore import *
from error_handling.functions import *

def corrupted_data(spark: SparkSession, out1: DataFrame) -> DataFrame:
    return out1.filter(
        (
          ((((col("account_id") == lit("")) | col("account_id").isNull()) | (col("region") == lit(""))) | (col("region").isNull() | (col("country") == lit(""))))
          | (
            (col("country").isNull() | (col("annual_revenue") == lit("N/A##")))
            | (
              (col("created_date") == lit("99-99-9999"))
              | (
                col("company_name")
                == lit(
                  "###CORRUPT###"
                )
              )
            )
          )
        )
    )
