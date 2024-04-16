import os
from box.exceptions import BoxValueError
import yaml
from llm_detection.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input
    Raises:
        valueError : if the yaml file is empty 
    Returns:
        ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
@ensure_annotations    
def create_directories(path_to_directories: list, verbrose=True):
    """
    create a list of directories 

    Args:
        path_to_directories:
        ignore_log
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbrose:
            logger.info(f"craeted directory at : {path}")
@ensure_annotations       
def get_size(path: Path) -> str:
    """

    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"