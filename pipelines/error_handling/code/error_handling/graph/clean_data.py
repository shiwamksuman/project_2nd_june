from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from error_handling.config.ConfigStore import *
from error_handling.functions import *

def clean_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(
        (
          (((col("account_id") != lit("")) & (col("region") != lit(""))) & (col("annual_revenue") != lit("N/A##")))
          & (
            (col("created_date") != lit("99-99-9999"))
            & (
              col("company_name")
              != lit(
                "###CORRUPT###"
              )
            )
          )
        )
    )
