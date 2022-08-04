"""
driver file is responsible for creating spark session, and handle user defined arguments.

"""

import argparse
import os

from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *

import utils.parse_config as parser
import utils.logger as logger
import scripts.execute as datasync

LOGGER = logger.get_logger('driver_file')

if __name__ == "__main__":
    # Parse app config file here.

    # Initialize parser
    args_parser = argparse.ArgumentParser()

    # Adding optional argument
    args_parser.add_argument("-r", "--resource", help = "resource config file name")
    args_parser.add_argument("-l", "--loaddate", help = "snapshot date", default="")
    args_parser.add_argument("-a2", "--arg2", help = "parameter 2 of resource config file to be used in sql", default="")
    args_parser.add_argument("-a3", "--arg3", help = "parameter 3 of resource config file to be used in sql", default="")
    args_parser.add_argument("-a4", "--arg4", help = "parameter 4 of resource config file to be used in sql", default="")
    args_parser.add_argument("-c", "--config", help = "path of app_config.yaml", default=os.path.dirname(__file__))
    args = args_parser.parse_args()

    #Read resource config here.
    LOGGER.info(logger.pretty_message('Application data-sync run started...'))

   

    # Read input type from configuration file and parse connection parameters and call that source
    # Create spark session
    spark = SparkSession \
        .builder \
        .appName("datasync_feature_calculation") \
        .config('spark.sql.sources.partitionOverwriteMode', 'dynamic') \
        .getOrCreate()
    spark.sparkContext.setLogLevel('WARN')

    print(args)

    datasync.calculateFeatures(args, spark)
    

    