"""
execute file will read the parquet file , transform data based on sql, and save the result to feature store.
"""

from datetime import datetime, timedelta
import os

from utils import logger
import utils.parse_config as parser
from pyspark.sql.functions import col, filter



LOGGER = logger.get_logger("transform_data")

def read_resource(task_file_name):
    # Get resources directory which holds all of the configuration files.
    resources_dir_path = f'{os.path.dirname(os.path.abspath(os.path.dirname(__file__)))}/resources'
    LOGGER.info(f"Reading file {task_file_name} from {resources_dir_path} directory...")
    resource_config = parser.get_yaml_file(resources_dir_path, task_file_name)

    return resource_config

def get_feature_start_date(load_date, feature_duration: str) -> str:
    """

    :return:
    """

    start_date = ''

    if feature_duration.upper() == '7D':
        load_date = datetime.strptime(load_date, '%Y-%m-%d')
        start_date = load_date - timedelta(days=7)
        LOGGER.info(
            f'Feature duration is {feature_duration} start_date is {str(start_date).split(" ")[0]} Till: {load_date}')
    elif feature_duration.upper() == '28D':
        load_date = datetime.strptime(load_date, '%Y-%m-%d')
        start_date = load_date - timedelta(days=28)
        LOGGER.info(
            f'Feature duration is {feature_duration} start_date is {str(start_date).split(" ")[0]} Till: {load_date}')
    elif feature_duration.upper() == 'ITD':
        start_date = '2018-01-01'

    return str(start_date).split(" ")[0]

def calculateFeatures(args, spark):
    """
    This function will read from parquet file and register dataframe as spark table
    """

    resource_config = read_resource(args.resource)
    start_date = get_feature_start_date(args.loaddate, resource_config.get('feature_time_window'))

    input_df = spark.read.parquet(resource_config.get('input_parquet_location')).filter(
        (col('start_date_est') >= start_date) & (col('start_date_est') < args.loaddate))

    # transform_data(spark, input_df, resource_config)

    input_df.createOrReplaceTempView(resource_config.get('name'))
    output_df = spark.sql(resource_config.get('sql').format(table_name = resource_config.get('name')))
    print(output_df.take(200))

    output_df.write.format('parquet').mode('overwrite').save(f'{resource_config.get("output_location")}/{args.loaddate}');
