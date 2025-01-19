from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]: # my function will return a  list
    '''
    this  function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  #during reading the requirements.txtx it will include \n so we replace it with blank...
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
    name = 'mlproject',
    version ='0.0.1',
    author ='prathik',
    author_email = 'hadagali2002@gmail.com',
    packages = find_packages(),
    install_requires =get_requirements('requirements.txt') #['pandas','numpy','seabron']
)
