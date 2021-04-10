from os import path
from setuptools import setup, find_packages


NAME = "test_actions"
DIRPATH = path.abspath(path.dirname(__file__))


with open(path.join(DIRPATH, AME, "_version.py")) as f:
    version = ".".join([i.strip() for i in f.read().splitlines()[-2].split("=")[1][2:-1].split(",")])
with open(path.join(DIRPATH, "README.md")) as f:
    long_description = f.read()
with open(path.join(DIRPATH, "requirements.txt")) as f:
    install_requires = f.read().splitlines()


setup(
    name=NAME,
    version=version,
    description="short description",
    long_description=long_description,
    include_package_data=True,
    package_data={},
    install_requires=install_requires,
    packages=find_packages(),
    url="test",
    author="test",
    author_email="test@protonmail.com"
)
