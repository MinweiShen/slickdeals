# Slickdeals
---

A command line tool for [Slickdeals](http://slickdeals.net).

## Dependency
1. requests
2. beautifulsoup

## Usage
python slickdeals.py [option]

### Options
1. ``-f --free``: show items free or ship free on frontpage
2. ``-F --FREE``: show items which are free on frontpage
3. ``-n NUM``: limit the number of results
4. ``-s 'search string'``: search item, quotation marks are required especially when your search string contains space


### Example
1. ``python slickdeals.py -F -n 10`` : show first 10 free items on frontpage
2. ``python slickdeals.py -s 'amazon xbox'`: search amazon xbox deals
3. ``python slickdeals.py -s 'amazon' -f -n 10``: search free amazon deals, show 10 results




