from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *

def filter_nonnull_oppid(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(col("opp_id").isNotNull())
