#!/usr/bin/env python

from setuptools import find_packages, setup

__version__ = '0.1.0'

requires = [
    'requests==2.13.0',
]

setup(
    name='tinymind-cli',
    version=__version__,
    description='CLI tool for TinyMind',
    author='TinyMind',
    author_email='hello@tinymind.ai',
    url='https://github.com/mind/cli',
    packages=find_packages(),
    install_requires=requires,
    keywords='tinymind',
)
