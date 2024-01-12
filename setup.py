#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='EDF-algorithm',
    version='0.1.0',
    description='A basic implementation of the EDF algorithm in python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Suren Lockwood',
    author_email='dev@behnamlal.xyz',
    url='https://github.com/CheesyChocolate/EDF-algorithm',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent"
        ],
    python_requires='>=3.6',
    install_requires=[
        'matplotlib',
                 ],
)
