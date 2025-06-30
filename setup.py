from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.
    """
    requirement_list:List[str] = []

    try:
        # Attempt to read the requirements from a file
        with open('requirements.txt', 'r') as file:
            # Read the requirements from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                # Strip whitespace and new lines, ignore comments
                requirement = line.strip()
                # Ignore  empty lines and -e .
                if requirement and not requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")


    
    return requirement_list
print(get_requirements())

setup(
    name = 'AI_Trip_Planner',
    version = '0.0.1',
    author = 'Praveen Kumar',
    author_email = 'praveenkumarg1499@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements(),
)