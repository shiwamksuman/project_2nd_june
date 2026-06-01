from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *

def bronze_products(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`main`.`prophecy_lh`.`bronze_products`")
