from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dup_ppl.config.ConfigStore import *
from dup_ppl.functions import *
from prophecy.utils import *
from dup_ppl.graph import *

def pipeline(spark: SparkSession) -> None:
    df_incremental_load = incremental_load(spark)
    bronze_daily_events(spark, df_incremental_load)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("daily_incremental_load").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/dup_ppl")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/dup_ppl", config = Config)(pipeline)

if __name__ == "__main__":
    main()
