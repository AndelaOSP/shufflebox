#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='shufflebox',
    version='0.1.0',
    description='A randomizer package for shuffling.',
    long_description=readme,
    author='Andela Kenya',
    author_email='herbert.kagumba@andela.com, githinji.gikera@andela.com',
    url='https://github.com/AndelaOSP/shufflebox',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
