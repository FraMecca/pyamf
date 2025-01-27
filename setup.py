#!/usr/bin/env python

# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

# import ordering is important
import setupinfo
from setuptools import setup, find_packages


version = (0, 8, 0)

name = "PyAMF"
description = "AMF support for Python"
long_description = setupinfo.read('README.rst')
url = "http://pyamf.org"
author = "The PyAMF Project"
author_email = "users@pyamf.org"
license = "MIT License"

classifiers = """
Framework :: Django
Framework :: Pylons
Framework :: Twisted
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: C
Programming Language :: Python
Topic :: Internet :: WWW/HTTP :: WSGI :: Application
Topic :: Software Development :: Libraries :: Python Modules
"""

keywords = """
amf amf0 amf3 flex flash remoting rpc http flashplayer air bytearray
objectproxy arraycollection recordset actionscript decoder encoder gateway
remoteobject twisted pylons django sharedobject lso sol
"""


def setup_package():
    setupinfo.set_version(version)

    setupinfo.write_version_py()

    setup(
        name=name,
        version=setupinfo.get_version(),
        description=description,
        long_description=long_description,
        url=url,
        author=author,
        author_email=author_email,
        keywords=keywords.strip(),
        license=license,
        packages=find_packages(),
        install_requires=setupinfo.get_install_requirements(),
        tests_require=setupinfo.get_test_requirements(),
        test_suite="pyamf.tests.get_suite",
        zip_safe=False,
        extras_require=setupinfo.get_extras_require(),
        classifiers=(
            [_f for _f in classifiers.strip().split('\n') if _f] +
            setupinfo.get_trove_classifiers()
        ),
        **setupinfo.extra_setup_args())


if __name__ == '__main__':
    setup_package()
