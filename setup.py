#/usr/bin/env python
import sys

from setuptools import setup
from {{ cookiecutter.name }} import VERSION

try:
    readme = open('README.rst')
    long_description = str(readme.read())
finally:
    readme.close()

required_pkgs = []
if sys.version_info < (2, 7):
    required_pkgs.append('argparse')

setup(
    name='{{ cookiecutter.name }}',
    version=VERSION,
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/{{ cookiecutter.name }}',
    packages=[
        '{{ cookiecutter.name }}',
    ],
    install_requires=required_pkgs,
    scripts=['scripts/{{ cookiecutter.name }}'],
    license='New BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    test_suite='tests'
)
