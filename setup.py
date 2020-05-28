
from setuptools import setup, find_packages

from os import path

def get_readme():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
        readme = readme_file.read()
    return readme

def get_requirements():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'requirements.txt'), encoding='utf-8') as \
        requirements_file:
        requirements = requirements_file.read().splitlines()
        return requirements

setup(
    name="py-multi-pager",
    version="0.2.0",
    author='Doyeon Kim',
    author_email='archdo0909@gmail.com',
    description="Easy and fast python SNS notifier.",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=get_requirements(),
    url='https://github.com/archdo0909/NotiPy',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
