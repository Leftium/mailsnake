#!/usr/bin/env python
from setuptools import setup, find_packages

import mailsnake

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'mailchimp api wrapper 1.3'


setup(name = 'mailsnake',
    version = mailsnake.__version__,
    description = """MailChimp API v1.3 wrapper for Python.""",
    author = mailsnake.__author__,
    url = "https://github.com/leftium/mailsnake",
    packages = find_packages(),
    download_url = "http://pypi.python.org/pypi/mailsnake/",
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    zip_safe = True,
    install_requires=['distribute']
)