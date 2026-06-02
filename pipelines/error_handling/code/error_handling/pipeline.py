from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from error_handling.config.ConfigStore import *
from error_handling.functions import *
from prophecy.utils import *
from error_handling.graph import *

def pipeline(spark: SparkSession) -> None:
    df_malformed = malformed(spark)
    df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_malformed)
    df_corrupted_data = corrupted_data(spark, df_RowDistributor_1_out1)
    bronze_corrupt_quarantine(spark, df_corrupted_data)
    df_clean_data = clean_data(spark, df_RowDistributor_1_out0)
    bronze_accounts_validated(spark, df_clean_data)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("error_handling").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/error_handling")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/error_handling", config = Config)(pipeline)

if __name__ == "__main__":
    main()
