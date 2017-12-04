#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import os
import sys
from io import open
from setuptools import setup, find_packages

VERSION = '0.1'

if sys.argv[-1] == 'publish':        
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    print("  git push --tags")
    sys.exit()

setup(
    name = 'wagtail-smartstream',
    version = VERSION,
    install_requires = (),
    author = 'Mitja Pagon',
    author_email = 'mitja@inueni.com',
    license = 'MIT',
    url = 'https://github.com/inueni/wagtail-smartstream/',
    keywords = 'wagtail admin streamfield django cms',
    description = 'Proof of concept Wagtail StreamFieldPanel that avoids unnecessary template rendering.',
    long_description = "",
    packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
    ]
)