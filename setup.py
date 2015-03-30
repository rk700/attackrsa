#!/usr/bin/env python

from setuptools import *

setup(
    name = 'attackrsa',
    version = '0.1',
    install_requires = ['gmpy'],
    packages = ['attackrsa'],
    scripts = ['bin/attackrsa']
)

    
