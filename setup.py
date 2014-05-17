#!/usr/bin/env python

from setuptools import setup

setup(
    name='AskFIT',
    version='1.0',
    description='FIT Stack Overflow',
    author='Miro Hroncok',
    author_email='miro@hroncok.cz',
    url='https://github.com/hroncok/askfit',
    license='GPLv3+',
    install_requires=[
        'Django==1.5',
        'psycopg2',
        'askbot',
        'django-rosetta',
    ]
)
