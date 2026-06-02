from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from error_handling.config.ConfigStore import *
from error_handling.functions import *

def bronze_accounts_validated(spark: SparkSession, clean_data: DataFrame):
    clean_data.write.format("delta").mode("overwrite").saveAsTable("`main`.`prophecy_lh`.`bronze_accounts_validated`")
