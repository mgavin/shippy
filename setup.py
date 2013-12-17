# -*- coding: utf-8 -*-
"""

Description:
Setup script for shippy
"""
from setuptools import setup, find_packages
from datetime import datetime

LONG_DESCRIPTION = \
"""A wrapper around Shipping Carrier's (FedEx, UPS, USPS) web services"""

CLASSIFIERS = [
                'Development Status :: 1 - Planning',
                'Intended Audience :: Developers',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules'
              ]

KEYWORDS = 'fedex ups usps shippy soap suds wrapper'

setup(
    name='shippy',
    version=str(datetime.date(datetime.today())),
    description = 'Carrier Web Services API wrapper.',
    long_description = LONG_DESCRIPTION,
    author = 'Matthew Gavin',
    author_email = 'matthew.ashton3@gmail.com',
    packages = find_packages(),
    platforms=['Platform Independent'],
    classifiers = CLASSIFIERS,
    keywords=KEYWORDS,
    requires=['suds', 'pytz', 'simplejson'],
    install_requires = ['suds', 'pytz', 'simplejson'],
    zip_safe = False,
    include_package_data = True
  )
