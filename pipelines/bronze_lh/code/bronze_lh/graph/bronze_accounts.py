from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *

def bronze_accounts(spark: SparkSession, non_null_accounts: DataFrame):
    non_null_accounts.write.format("delta").mode("overwrite").saveAsTable("`main`.`prophecy_lh`.`bronze_accounts`")
