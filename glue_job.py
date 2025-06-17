# To Monitor the Glue job from the AWS console after CI run

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://your-bucket/raw-data/"], "recurse": True},
    format_options={"withHeader": True}
)

mapped = ApplyMapping.apply(df, mappings=[
    ("column1", "string", "column1", "string"),
    ("column2", "int", "column2", "int")
])

glueContext.write_dynamic_frame.from_options(
    frame=mapped,
    connection_type="s3",
    format="csv",
    connection_options={"path": "s3://your-bucket/processed-data/"}
)

job.commit()


