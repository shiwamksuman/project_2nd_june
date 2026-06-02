from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from daily_incremental_load.config.ConfigStore import *
from daily_incremental_load.functions import *

def incremental_load(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("parquet")\
        .option("mergeSchema", True)\
        .load("dbfs:/Volumes/main/prophecy_lh/daily_events/prophecy_lakehouse_datasets/daily_events/")
