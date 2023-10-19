# -*- coding: utf-8 -*-
"""Please directly install `lighteval` instead."""

from __future__ import print_function, unicode_literals

import os
import warnings
import sys
from distutils.command.install import install

# version string
__version__ = '0.0.1'


class Install(install):
    """Magic install command."""

    def check_call(self, cmd):  # pylint: disable=no-self-use
        """Wrapper for functionality of `subprocess.check_call`."""
        return_code = os.system(cmd)
        if return_code != 0:
            raise OSError('[EXIT %s] %s' % (return_code, cmd))

    def run(self):  # pylint: disable=no-self-use
        if False:
            raise RuntimeError('This is a dummy package for `lighteval`. '
                               'Please directly install `lighteval` instead.')
        else:
            print(u'This is a dummy package for `lighteval`.', file=sys.stderr)
            print(u'Trying to reinstall...', file=sys.stderr)
            try:
                self.check_call('%s -m pip install lighteval' % sys.executable)
            except OSError:
                print(u'Failed to reinstall...', file=sys.stderr)
                print(u'Please directly install `lighteval` instead.', file=sys.stderr)
                raise
            print(u'Successfully reinstalled...', file=sys.stderr)


# setup attributes
attrs = dict(
    name='lighteval',
    version=__version__,
    description='Dummy package for lighteval.',
    long_description=__doc__,
    author='Lighteval Team',
    author_email='clementine@huggingface.co',
    maintainer='Lighteval Team',
    maintainer_email='clementine@huggingface.co',
    url='https://github.com/huggingface/lighteval',
    # download_url
    py_modules=['lighteval'],
    # scripts
    # ext_modules
    classifiers=[
        'Development Status :: 7 - Inactive',
    ],
    # distclass
    # script_name
    # script_args
    # options
    license='The Unlicensed',
    keywords=[
        'dummy',
        'lighteval',
        'lighteval',
    ],
    platforms=[
        'any'
    ],
    cmdclass=dict(
        install=Install,
    ),
    # data_files
    # package_dir
    # obsoletes
    # provides
    # requires
    # command_packages
    # command_options
    package_data={
        '': [
            'LICENSE',
            'README.md',
        ],
    },
    # include_package_data
    # libraries
    # headers
    # ext_package
    # include_dirs
    # password
    # fullname
    # long_description_content_type
    # python_requires
    # zip_safe,
    # install_requires
)

try:
    from setuptools import setup

    attrs.update(dict(
        include_package_data=True,
        # libraries
        # headers
        # ext_package
        # include_dirs
        # password
        # fullname
        long_description_content_type='text/markdown',
        # python_requires
        zip_safe=True,
    ))
except ImportError:
    from distutils.core import setup

# set-up script for pip distribution
setup(**attrs)

# warn about the package
warnings.warn('This is a dummy package for `lighteval`. '
              'Please directly install `lighteval` instead.')
