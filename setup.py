#!/usr/bin/env python

from setuptools import setup

def readme():
    with open("README.rst") as it:
        return it.read()

if __name__ == '__main__':
    setup(
        name = 'termcolor2',
        version = '0.0.1',
        description = 'simple termcolor wrapper',
        long_description = readme(),
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/v2e4lisp/termcolor2',
        requires = ["termcolor"],
        py_modules = ["termcolor2"]
    )
