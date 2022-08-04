import json
import os
from typing import Any, Dict, List, Tuple
import yaml
import zipfile


def get_yaml_file(path: str, filename) -> Dict[str, Any]:
    """
    Parse yaml file to json

    Args:
        path (str):  Path of yaml file
        filename (str): Yaml filename to be parsed

    Return:
        (Dict[str, Any]): Json parsed from yaml file
    """

    # Check if our yaml file is inside egg file if it is inside egg file we need to use zip module
    # to open the file. We cannot use normal open method
    if path.find('.egg') != -1:        
        try:
            with zipfile.ZipFile(f'{"/".join(path.split("/")[0:-1])}') as myzip:                
                with myzip.open(f'resources/{filename}', 'r') as get_yaml:
                    return yaml.load(get_yaml, Loader=yaml.FullLoader)  # nosec
        except FileNotFoundError as file_not_found_error:
            raise FileNotFoundError(f'{path}/{filename} file not found in your egg file. ',
                            'Please see documentation for more details.') from file_not_found_error

    try:
        with open(os.path.expanduser(f'{path}/{filename}'), 'r') as get_yaml:
            return yaml.load(get_yaml, Loader=yaml.FullLoader)  # nosec
    except FileNotFoundError as file_not_found_error:
        raise FileNotFoundError(f'{path}/{filename} file not found... ',
                                'Please see documentation for more details.') from file_not_found_error
