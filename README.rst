keyutil
=======

keyutil is a Python package which is used to generate SECRET_KEYs to secure
session data.

Most of the code is taken from the Django project, specifically
``django.core.management.utils`` and ``django.utils.crypto``.

.. _installation:

Installation
------------

Supported versions of Python are: 2.7, 3.3, 3.4, and 3.5. The recommended way
to install this package is via `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: bash

    $ git clone https://github.com/lukassup/keyutil.git
    $ pip install ./keyutil

For instructions on installing python and pip see "The Hitchhiker's Guide to
Python" `Installation Guides
<http://docs.python-guide.org/en/latest/starting/installation/>`_.

.. _usage:

Usage
-----

.. code-block:: bash

    $ python -m keyutil
    SECRET_KEY = 'yp1uz^!i83*y1h8fty5gpxs3u-i%zzs@lbk#-j!&t2h$zlc(9v'
