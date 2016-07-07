Slickdeals
==========

A command line tool for `Slickdeals`_

Dependency
-----------
1) requests
2) beautifulsoup

How to install
--------------
::
    pip install slickdeals
or
::
    python setup.py install

Usage
-------
::
    slickdeals [option]

Options
--------
1) -f --free: show items free or ship free on frontpage
2) -F --FREE: show items which are free on frontpage
3) -n NUM: limit the number of results
4) -s 'search string': search item, quotation marks are required especially when your search string contains space


Example
--------
1) show first 10 free items on frontpage::
    slickdeals -F -n 10
2) search amazon xbox deals::
    slickdeals -s 'amazon xbox'
3) search free amazon deals, show 10 results::
    slickdeals.py -s 'amazon' -f -n 10

.. _Slickdeals: http://slickdeals.net




