from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from error_handling.config.ConfigStore import *
from error_handling.functions import *

def bronze_corrupt_quarantine(spark: SparkSession, corrupted_data: DataFrame):
    corrupted_data.write.format("delta").mode("append").saveAsTable("`main`.`prophecy_lh`.`bronze_corrupt_quarantine`")
