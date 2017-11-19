from setuptools import setup, find_packages

from codecs import open
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the installation requirements from reqs_install.dep file
with open(path.join(here, 'reqs_install.dep'), encoding='utf-8') as f:
    install_requires = f.readlines()

setup(
    name='pynflate',
    version='1.0.0',

    description='Humane grammar library',
    long_description=long_description,
    url='https://github.com/yanivmo/ruler',
    license='MIT',

    # Add all packages under src
    packages=find_packages('src'),
    # src is the root directory for all the packages
    package_dir={'': 'src'},

    install_requires=install_requires,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',

        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='compression decompression deflate lz77 huffman'
)
