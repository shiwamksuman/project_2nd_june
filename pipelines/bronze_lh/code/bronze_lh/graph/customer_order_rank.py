from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *

def customer_order_rank(spark: SparkSession, sales_transactions: DataFrame) -> DataFrame:
    return sales_transactions\
        .withColumn("order_rank", row_number().over(Window.partitionBy(col("customer_id")).orderBy(col("order_date").asc())), )\
        .withColumn("prev_amount", lag(col("amount"), 1).over(Window.partitionBy(col("customer_id")).orderBy(col("order_date").asc())), )
