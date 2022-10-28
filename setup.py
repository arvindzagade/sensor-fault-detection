"""
This file is created because we want our own packages to be installed once we execute the code.
"""
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    """
    Assignment:
     write a code to read requirement.txt file and append each requirement in requirement_list variable.

    """
    return requirement_list
    
setup(
    name= "sensor",
    version="0.0.1",
    author="ineuron",
    author_email="a@gmail.com",
    packages= find_packages(),
    install_requires =get_requirements(),#[],
)