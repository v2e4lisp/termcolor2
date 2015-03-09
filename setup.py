#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    readme = open("README.rst").read()
    setup(
        name = 'termcolor2',
        version = '0.0.3',
        description = 'simple termcolor wrapper',
        long_description = readme,
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/v2e4lisp/termcolor2',
        install_requires = ["termcolor"],
        py_modules = ["termcolor2"]
    )
