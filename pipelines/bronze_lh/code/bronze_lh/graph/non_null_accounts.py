from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *

def non_null_accounts(spark: SparkSession, accounts: DataFrame) -> DataFrame:
    return accounts.filter(col("account_id").isNotNull())
