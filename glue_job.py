# Minimal AWS Glue Spark job for the CloudFormation lab.
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glue_context = GlueContext(sc)
spark = glue_context.spark_session

data = [(1, 'dhevan'), (2, 'ali'), (3, 'Charlie')]
df = spark.createDataFrame(data, ['id', 'name'])
df.show()
print('Glue data processing completed successfully with error code 0')
