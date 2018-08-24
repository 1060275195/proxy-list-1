import sys
import urllib2
from bs4 import BeautifulSoup

proxy_page = 'https://www.socks-proxy.net/'
proxy_hdr = {'User-Agent': 'Mozilla/5.0'}
proxy_req = urllib2.Request(proxy_page, headers=proxy_hdr)

page = urllib2.urlopen(proxy_req)
soup = BeautifulSoup(page, 'html.parser')

proxy_table = soup.find('table')
proxy_row = soup.find_all('tr')


def generate_proxy_chain():

    if len(sys.argv) < 2:
        # Configure the default number of hops you want here.
        # Recommend at least 5, but more than 10-15 will be super slow
        number_of_rows = 5
    else:
        if sys.argv[1].isdigit():
            number_of_rows = sys.argv[1]
        else:
            err = """
                Invalid number of proxies for the chain.
                Please provide an integer."""
            raise ValueError(err)
            return -1

    outFile = open('output.txt', 'w')

    for i in range(1, int(number_of_rows) + 1):
        currentProxyData = proxy_row[i].find_all('td')

        proto = currentProxyData[4].string.lower()
        ip_addr = currentProxyData[0].string
        port = currentProxyData[1].string

        currentRow = '{}  {}  {}'.format(proto, ip_addr, port)
        outFile.write(currentRow + '\n')

    outFile.close()
    return 0


generate_proxy_chain()
