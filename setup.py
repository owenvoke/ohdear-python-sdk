#!/usr/bin/env python3

from setuptools import setup

setup(
    name='ohdear-sdk',
    packages=['ohdear'],
    version='0.2.0',
    install_requires=['requests'],
    description='Oh Dear Python SDK',
    author='Owen Voke',
    url='https://github.com/owenvoke/ohdear-python-sdk',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
