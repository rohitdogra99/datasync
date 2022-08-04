"""
This python file will parse the resource file name passed using --resource parameter
"""

import os

from pyspark.sql.types import *

import utils.logger as logger
import utils.parse_config as parser
import config.snowflake_config as snow_config
import src.read_snowflake as snowflake
import destination.write_parquet as par


LOGGER = logger.get_logger("parse_resource_file_provided")

def parse_resource(spark,args):
    """
    This function will parse resource file provided by user using --resource argument.
    And call the corresponding function.
    :spark : Spark Session
    :args  : argument provided by user
    :return: 0
    """

    resources_dir_path = f'{os.path.dirname(os.path.abspath(os.path.dirname(__file__)))}/resources'
    LOGGER.info(f"Reading file {args.resource} from {resources_dir_path} directory...")
    resource_config = parser.get_yaml_file(resources_dir_path, args.resource)
    source_type = resource_config.get("sourceType")
    target_type = resource_config.get("targetType")

    LOGGER.info(f'Input type is {source_type} and target type is {target_type}')

    columns = StructType([])

    # Create an empty dataframe with empty schema
    input_df = spark.createDataFrame(data = [],
                                     schema = columns)

    if source_type.upper() == 'SNOWFLAKE':
        LOGGER.info("Input type is snowflake...")
        # Read snowflake credentials in dict
        snowflake_opts = snow_config.snowflake_options
        input_df = snowflake.read_from_snowflake(spark, snowflake_opts, args)
        print(input_df.printSchema())
        print(input_df.show())
    else:
        raise Exception(f"Source Type {source_type} is not supported currently Supported types for source are \n 1) snowflake")

    if target_type.upper() == 'PARQUET':
        par.write_df_to_parquet(input_df, args)
    return 0
