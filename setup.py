from setuptools import find_packages, setup
from typing import List


"""
this script is to make src dir an installable pythod package. this is a very best practice
that allwos you to use clean imports like from "src.components.model_trainer import ModelTrainer"
from anywhere from the project
"""
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of package requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Krishna Pole',
    author_email='krishnapole90@gmail.com',
    description='A machine learning project template',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
