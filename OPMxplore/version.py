from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "OPMxplore: exploring membrane proteins"
# Long description will go up on the pypi page
long_description = """

OPMxplore
========
OPMxplore is a tool for analyzing membrane proteins from the
Orientations of Proteins in Membranes (OPM) database:
http://opm.phar.umich.edu/

It allow users to perform custom queries of the OPM database.
It uses pypdb to search the RCSB proteins database, 
and cross-reference the results with the OPM database:
https://www.rcsb.org/pdb/home/home.do
https://github.com/williamgilpin/pypdb

Once the desired proteins are identified, pdb-search provides tools to 
analyze and compare the results using interactive plotly graphs:
https://plot.ly/

Furthermore, individual proteins can be visualized within a 
Jupyter-notebook using nglview:
https://github.com/arose/nglview

To find out more about the project, please go to the repository README_:

.. _README: https://github.com/UWSEDS-aut17/OPMxplore/blob/master/README.md

License
=======
``OPMxplore`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2017--, David Starkebaum, Felcy Selwyn, Sinduja Karl Marx, 
The University of Washington eScience Institute.
"""

NAME = "OPMxplore"
MAINTAINER = "David Starkebaum"
MAINTAINER_EMAIL = "dasman@uw.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/UWSEDS-aut17/OPMXplore"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "David Starkebaum, Felcy Selwyn, Sinduja Karl Marx"
AUTHOR_EMAIL = "dasman@uw.edu, felcy@uw.edu, skmarx@uw.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'OPMxplore': [pjoin('data', '*')]}
REQUIRES = ["numpy", 
            "scipy", 
            "matplotlib", 
            "pandas", 
            "pypdb", 
            "nglview", 
            "biopython", 
            "biopandas",
            "pandasql",
            "plotly"]
