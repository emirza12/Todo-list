#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='Todo-list',
    version='1.0',
    author='emirza12',
    license='MIT',
    packages=find_packages(),
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'todo=todo:main',
        ],
    },
)