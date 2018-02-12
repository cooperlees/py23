#!/usr/bin/env python3

from py23 import __version__
from setuptools import setup
from sys import version

# Add typing if we're unfortunately Python 2
INSTALL_REQUIRES = ['click', 'future', 'six']
if version[0] == '2':
    INSTALL_REQUIRES.append('typing')

setup(
    name='py23',
    version=__version__,
    packages=['py23'],
    url='http://github.com/cooperlees/py23',
    license='MIT',
    author='Cooper Lees',
    author_email='me@cooperlees.com',
    description='Sample code to show the people how to Py2 to Py3',
    classifiers=(
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Development Status :: 3 - Alpha',
    ),
    install_requires=[],
    tests_require=['pytest', 'tox'],
    entry_points={
        'console_scripts': [
            'py23 = py23.py23:main'
        ]
    },
    test_suite='py23.tests.base',
)
