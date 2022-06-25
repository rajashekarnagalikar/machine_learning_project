from setuptools import setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "RAJ"
DESCRIPTION = "This is the first FSDS Nov batch machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_lists()->List[str]:
    """ 
    Description: This function is going to return list of requirement 
    mentioned in requirements.txt file

    return This function is going to return  a list which contains name of libraries 
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_lists()
)
