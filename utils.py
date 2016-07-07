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

    return parser.parse_args()


def crawl_deals():
    options, args = parse_command()
    show_free = options.show_free
    show_free_price = options.show_free_price
    r = requests.get(SLICKDEALS)
    soup = BeautifulSoup(r.text, 'html.parser')

    fpdeals = soup.find_all('div', {'class': 'frontpage'})
    deals = []
    for d in fpdeals:
        a = d.find('a', {'class': 'itemTitle'})
        link = SLICKDEALS + a['href']
        price_line = d.find('div', {'class': 'priceLine'})
        title = price_line['title']
        price_div = price_line.find('div', {'class': 'itemPrice'})
        price = price_div and price_div.string.strip().lower() or 'None'
        shipinfo_div = price_line.find('div', {'class': 'priceInfo'})
        shipinfo = shipinfo_div and shipinfo_div.string.strip().lower() or 'None'
        item = {
            'title': title,
            'link': link,
            'price': price,
            'shipinfo': shipinfo
        }
        if show_free_price:
            if 'free' in price:
                deals.append(item)
        elif show_free:
            if 'free' in shipinfo or 'free' in price:
                deals.append(item)
        else:
            deals.append(item)
    if options.num:
        deals = deals[:options.num]
    return deals



