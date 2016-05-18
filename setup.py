#!/usr/bin/env python
# Copyright (C) 2016  graypawn <choi.pawn @gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from yusuke import __version__
from setuptools import setup, find_packages

install_requires = [
]

tests_requires = [
]

setup(
    name='yusuke',
    version=__version__,
    description='pacman update notifier',
    author='graypawn',
    author_email='choi.pawn' '@gmail.com',
    url='https://github.com/graypawn/yusuke',
    license='GPL3+',
    packages=find_packages(),
    install_requires = install_requires,
    tests_requires = tests_requires,
    classifiers = ["Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Operating System :: POSIX :: Linux",
                   "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"],
    entry_points={
        'console_scripts': [
            'yusuke=yusuke.__main__:main'
        ]
    }
)
