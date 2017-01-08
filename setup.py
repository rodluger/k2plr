#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

# Hackishly inject a constant into builtins to enable importing of the
# module.
if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins
builtins.__KPLR_SETUP__ = True
import k2plr

long_description = \
"""
A fork of the `kplr` package with custom `K2` functionality.
Enables access to the `K2` raw and de-trended light curves.
"""

setup(
    name="k2plr",
    version=k2plr.__version__,
    author="Daniel Foreman-Mackey (forked by Rodrigo Luger)",
    author_email="rodluger@uw.edu",
    packages=["k2plr"],
    url="https://github.com/rodluger/k2plr",
    license="MIT",
    description="Tools for working with Kepler and K2 data in Python",
    long_description=long_description,
    install_requires=["six"],
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
