#!/usr/bin/env python3

from setuptools import setup
from pathlib import Path

setup(
    name='ohdear-sdk',
    packages=['ohdear'],
    version='0.3.1',
    install_requires=['requests'],
    description='Oh Dear Python SDK',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    author='Owen Voke',
    author_email='development@voke.dev',
    url='https://github.com/owenvoke/ohdear-python-sdk',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
