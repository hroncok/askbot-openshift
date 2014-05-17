#!/usr/bin/env python

from setuptools import setup

setup(
    name='askbot-openshift',
    version='1.0',
    description='Askbot running on OpenShift',
    author='Miro Hroncok',
    author_email='miro@hroncok.cz',
    url='https://github.com/hroncok/askfit',
    license='GPLv3+',
    install_requires=[
        'Django==1.5',
        'psycopg2',
        'askbot',
        'django-rosetta',
        'django-redis-cache',
        'hiredis',
    ]
)
