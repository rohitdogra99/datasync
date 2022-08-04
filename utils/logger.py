"""
With the logging module imported, you can use a “logger” to log messages that you want to see.

Example:
        LOGGER = logger.get_logger('example')
"""
import logging


def get_logger(class_name):
    """
    The function allows you to use logger to different files

    Args:
        class_name (str): name of the class/file

    Return:
        logger (obj): Logger object instance
    """
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def pretty_message(text: str) -> str:
    """
    This is to prettify a text of a module.

    Args:
        text (str): Module name

    Return:
        (str): Pretty message banner
    """
    return (f'\n{"":*<108}\n*{"*":>107}\n*{"*":>107}\n*{text:^106}*\n'
            f'*{"*":>107}\n*{"*":>107}\n{"":*<108}')


def sub_message(text: str) -> str:
    """
    This is to prettify a text of a submodule.

    Args:
        text (str): Submodule name

    Return:
        (str): Sub module message banner
    """
    return f'\n{"":*<108}\n*{"*":>107}\n*{text:^106}*\n*{"*":>107}\n{"":*<108}'
