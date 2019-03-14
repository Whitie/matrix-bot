#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import matrix_bot


setup(
    name='matrix-bot',
    version=matrix_bot.__version__,
    description='One file library to create matrix bots (https://matrix.org).',
    long_description=matrix_bot.__doc__,
    long_description_content_type='text/markdown',
    author=matrix_bot.__author__,
    author_email='weimann.th@yahoo.com',
    url='https://github.com/whitie/matrix-bot',
    py_modules='matrix_bot',
    scripts=['matrix_bot.py'],
    install_requires=['matrix-client'],
    license=matrix_bot.__license__,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
