from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from bronze_lh.config.ConfigStore import *
from bronze_lh.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

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
