# this file is use for create basic structure for project

import os
from pathlib import Path # gives path for same format as Linux
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

package_name = "PhishingDomainDetection"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",   # unit test use for testing function and class
    "tests/integration/__init__.py",   # testing whole pipeline or two or more components or files
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt", # this file is used for devloper and testing
    "setup.py",
    "setup.cfg",
    "pyproject.toml",  # use for python package
    "tox.ini",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # give foldername and filename saprate
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"createing {filedir} for {filename}")

    # filesize must be zero and file must not be created then run this if
    # if file size is > 0 not override file
    # if file exists not override file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # one condition should fine don't write this two condition
        with open(filepath, "w") as f:
            pass # create empty file
        logging.info(f"creating empty file {filename}")
    else:
        logging.info(f"file {filename} successfully created")
