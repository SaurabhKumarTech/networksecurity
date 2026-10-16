from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """ This function wil return  list of requirements
    """
    requirements_list:List[str]=[]
    try:
        with open ("requirements.txt",'r') as file:
            #Read lines from the file
            lines=file.readlines()
            #procecc each line
            for line in lines:
                requirements= line.strip()
                ##ignore empty lines and -e
                if requirements and requirements!="-e .":
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

        return requirements_list   
setup(
    name="NetworkSecurity",
    version="0.01",
    author="Saurabh",
    packages=find_packages(),
    install_requires=get_requirements()
)              

        