from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from daily_incremental_load.config.ConfigStore import *
from daily_incremental_load.functions import *

def bronze_daily_events(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("append").saveAsTable("`main`.`prophecy_lh`.`bronze_daily_events`")
