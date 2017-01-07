# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='pullword',
    version='0.3.1',
    keywords=('pullword'),
    description='the sdk for pullword.com -- a free online\
                    Chinese text segmentation platform',
    license='MIT License',
    install_requires=['requests>=1.0.0'],
    author='sevenguin',
    packages=find_packages(),
    platforms='any',
)
