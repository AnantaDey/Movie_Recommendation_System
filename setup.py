from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(File_path: str) -> List[str]:
    requirements = []
    with open(File_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="movie_recommendation_projects",
    version="0.0.1",
    author="Ananta",
    author_email="ksadey1972@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt"),
)
