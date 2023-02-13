import os
import yaml
from pathlib import Path
from ensure import ensure_annotations
# with help of ConfigBox we can get dictinory keys using dict.key - more refere trails.ipynb
from box import ConfigBox
from box.exceptions import BoxValueError
from PhishingDomainDetection import log
import json

# ensure_annotation verifies that function output will be -> annotation type output 
# because we mention in annotation type -> ConfigBox type - more refere trails.ipynb
@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:  # so in annotation type we get ConfigBox dictinory
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path of input file
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            log.info(f"yaml file {path_to_yaml} load  successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            log.info(f"created directory at {path}")


def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"report are saved in {report_path}")
