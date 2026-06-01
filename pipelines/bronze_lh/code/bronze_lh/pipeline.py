from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *
from prophecy.utils import *
from bronze_lh.graph import *

def pipeline(spark: SparkSession) -> None:
    df_products = products(spark)
    df_valid_product_ids = valid_product_ids(spark, df_products)
    df_accounts = accounts(spark)
    df_non_null_accounts = non_null_accounts(spark, df_accounts)
    df_opportunities = opportunities(spark)
    df_filter_nonnull_oppid = filter_nonnull_oppid(spark, df_opportunities)
    bronze_products(spark, df_valid_product_ids)
    bronze_opportunities(spark, df_filter_nonnull_oppid)
    bronze_accounts(spark, df_non_null_accounts)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("bronze_lh").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/bronze_lh")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/bronze_lh", config = Config)(pipeline)

if __name__ == "__main__":
    main()
