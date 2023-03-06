#!/usr/bin/env python

from distutils.core import setup

from spc_spectra import __version__ as spc_version
from spc_spectra import __doc__ as spc_doc
from spc_spectra import __version__ as spc_version
from spc_spectra import __author__ as spc_author
from spc_spectra import __author_email__ as spc_author_email

setup(name='spc-spectra',
      version=spc_version,
      description=spc_doc,
      author=spc_author,
      author_email=spc_author_email,
      url='https://github.com/NickMacro/spc-spectra',
      download_url='https://github.com/NickMacro/spc-spectra/archive/0.4.0.tar.gz',
      packages=['spc_spectra'],
      classifiers=[],
      )
