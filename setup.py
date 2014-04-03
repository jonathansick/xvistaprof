#!/usr/bin/env python
# encoding: utf-8

import codecs
import os

from setuptools import setup, find_packages


PACKAGE = "xvistaprof"
NAME = "xvistaprof"
DESCRIPTION = "Astropy reader for XVISTA profile tables"
AUTHOR = "Jonathan Sick"
AUTHOR_EMAIL = "jonathansick@mac.com"
URL = "http://jonathansick.ca"
VERSION = __import__(PACKAGE).__version__


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
        ],
    zip_safe=False,
)
