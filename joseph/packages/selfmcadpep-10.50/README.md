   <p align="center">
      <a href="https://pypi.org/project/selfmcadpep"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/selfmcadpep.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/selfmcadpep"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/selfmcadpep.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/selfmcadpep/selfmcadpep"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/selfmcadpep/selfmcadpep.svg" /></a>
      <a href="https://github.com/selfmcadpep/selfmcadpep/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/selfmcadpep/selfmcadpep/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/selfmcadpep/selfmcadpep"><img alt="Build Status on Travis" src="https://travis-ci.org/selfmcadpep/selfmcadpep.svg?branch=master" /></a>
      <a href="https://selfmcadpep.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/selfmcadpep/badge/?version=latest" /></a>
   </p>

selfmcadpep is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses selfmcadpep and you should too.
selfmcadpep brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

selfmcadpep is powerful and easy to use:

.. code-block:: python

    >>> import selfmcadpep
    >>> http = selfmcadpep.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

selfmcadpep can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install selfmcadpep

Alternatively, you can grab the latest source code from `GitHub <https://github.com/selfmcadpep/selfmcadpep>`_::

    $ git clone https://github.com/selfmcadpep/selfmcadpep.git
    $ cd selfmcadpep
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

selfmcadpep has usage and reference documentation at `selfmcadpep.readthedocs.io <https://selfmcadpep.readthedocs.io>`_.


Contributing
------------

selfmcadpep happily accepts contributions. Please see our
`contributing documentation <https://selfmcadpep.readthedocs.io/en/latest/contributing.html>`_
for some tips on getting started.


Security Disclosures
--------------------

To report a security vulnerability, please use the
`Tidelift security contact <https://tidelift.com/security>`_.
Tidelift will coordinate the fix and disclosure with maintainers.


Maintainers
-----------

- `@sethmlarson <https://github.com/sethmlarson>`__ (Seth M. Larson)
- `@pquentin <https://github.com/pquentin>`__ (Quentin Pradet)
- `@theacodes <https://github.com/theacodes>`__ (Thea Flowers)
- `@haikuginger <https://github.com/haikuginger>`__ (Jess Shapiro)
- `@lukasa <https://github.com/lukasa>`__ (Cory Benfield)
- `@sigmavirus24 <https://github.com/sigmavirus24>`__ (Ian Stapleton Cordasco)
- `@shazow <https://github.com/shazow>`__ (Andrey Petrov)

👋


Sponsorship
-----------

If your company benefits from this library, please consider `sponsoring its
development <https://selfmcadpep.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for selfmcadpep is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-selfmcadpep?utm_source=pypi-selfmcadpep&utm_medium=referral&utm_campaign=readme
