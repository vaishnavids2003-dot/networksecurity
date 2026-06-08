'''This setup.py file is an essential part of pacakaging and distributing 
python projects. It is used by setuptools(or disutils in older python versions ) to define the 
configuration of the project such as metadata and dependencies.'''


from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return teh list of requirements
    '''
    requirement_lst: List[str] = []    
    try:
        with open('requirements.txt','r') as file :
            #Read line from the file.
            lines= file.readlines()
            #Process each line
            for line in lines:
                requirement= line.strip()
                #ignore -e. and empty lines
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found.')
    
    return requirement_lst
print(get_requirements())  

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Vaishnavi',
    author_email='<vaishnavi.ds2003@gmail.com>',
    packages=find_packages(),
    install_requires=get_requirements(),
)
