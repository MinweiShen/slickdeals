#! -*- encoding: utf-8 -*-
from optparse import OptionParser
import requests
from bs4 import BeautifulSoup

SLICKDEALS = 'http://slickdeals.net'


def parse_command():
    parser = OptionParser()
    parser.add_option('-f', '--free', action='store_true',
                      dest='show_free',
                      help='show deals free or ship free')
    parser.add_option('-F', '--FREE', action='store_true',
                      dest='show_free_price',
                      help='show free deals only')
    parser.add_option('-n', action='store', type='int',
                      dest='num', help='limit the num of results')
    parser.add_option('-s', '--search', action='store',
                      type='string', dest='search_for',
                      help='search \'item\', quotation marks are required')

    return parser.parse_args()


def crawl_front_page(options, args):
    show_free = options.show_free
    show_free_price = options.show_free_price
    r = requests.get(SLICKDEALS)
    soup = BeautifulSoup(r.text, 'html.parser')

    removeHidden = soup.find_all('div', {'class': 'removeHidden'})
    fpdeals = []
    for r in removeHidden:
        fpdeals += r.find_all('div', {'class': 'frontpage'})
    deals = []

    for d in fpdeals:
        a = d.find('a', {'class': 'itemTitle'})
        link = SLICKDEALS + a['href']
        price_line = d.find('div', {'class': 'priceLine'})
        title = price_line['title']
        price_div = price_line.find('div', {'class': 'itemPrice'})
        price = price_div and price_div.getText().strip() or 'None'
        shipinfo_div = price_line.find('div', {'class': 'priceInfo'})
        shipinfo = shipinfo_div and shipinfo_div.getText().strip() or 'None'
        item = {
            'title': title,
            'link': link,
            'price': price,
            'info': shipinfo
        }
        if show_free_price:
            if 'free' in price.lower():
                deals.append(item)
        elif show_free:
            if 'free' in shipinfo.lower() or 'free' in price.lower():
                deals.append(item)
        else:
            deals.append(item)
    if options.num:
        deals = deals[:options.num]
    return deals


def crawl_search_page(options, args):
    search_for = options.search_for.replace(' ', '+')
    url = SLICKDEALS+'/newsearch.php?src = SearchBarV2&q='+search_for
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find('div', {'data-module-name': 'Search Results'})
    results = results.find_all('div', {'class': 'resultRow'})
    deals = []
    for r in results:
        a = r.find('a', {'class': 'dealTitle'})
        title = a['title']
        link = SLICKDEALS + a['href']
        price = r.find('span', {'class': 'price'}).getText().strip()
        rating = r.find('div', {'class': 'ratingNum'}).getText().strip()
        expired = 'Expired' if 'expired' in r['class'] else ''
        item = {
            'title': title,
            'link': link,
            'price': price,
            'info': rating + ' ' + expired
        }
        if options.show_free or options.show_free_price:
            if 'free' in price.lower():
                deals.append(item)
        else:
            deals.append(item)

    if options.num:
        deals = deals[:options.num]
    return deals


def crawl_deals():
    options, args = parse_command()
    if options.search_for:
        return crawl_search_page(options, args)
    else:
        return crawl_front_page(options, args)




