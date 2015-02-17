#!/usr/bin/env python
from sys import platform
import setuptools

PROJECT_VERSION = '0.11.0'
PROJECT_URL = "https://github.com/nabla-c0d3/sslyze"
PROJECT_EMAIL = 'nabla.c0d3@gmail.com'
PROJECT_DESC = 'Fast and full-featured SSL scanner'

NASSL_BINARY = '_nassl.so'
if platform == 'win32':
    NASSL_BINARY = '_nassl.pyd'


SSLYZE_SETUP = {
    'name' : 'SSLyze',
    'version' : PROJECT_VERSION,
    'description' : PROJECT_DESC,
    'long_description' : open('README.md').read() + '\n' + open('AUTHORS.txt').read(),
    'author_email' : PROJECT_EMAIL,
    'url' : PROJECT_URL,
    'scripts' : ['sslyze.py'],
    'py_modules' : ['sslyze'],
    'packages' : ['plugins', 'utils'],
    'package_data' : {'plugins' : ['data/trust_stores/*.pem','data/trust_stores/mozilla_ev_oids.py'],},
    'license' : open('LICENSE.txt').read()
}

setuptools.setup(**SSLYZE_SETUP)
