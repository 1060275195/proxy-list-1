import urllib2
from bs4 import BeautifulSoup

proxy_page = 'https://www.socks-proxy.net/'
proxy_hdr = {'User-Agent': 'Mozilla/5.0'}
proxy_req = urllib2.Request(proxy_page, headers=proxy_hdr)

page = urllib2.urlopen(proxy_req)
soup = BeautifulSoup(page, 'html.parser')

proxy_table = soup.find('table')
proxy_row = soup.find_all('tr')

outFile = open('output.txt', 'a')

# Configure the number of hops you want here.
# Recommend at least 5, but more than 10-15 will be super slow
number_of_rows = 10

for i in range(1, number_of_rows + 1):
    currentProxyData = proxy_row[i].find_all('td')
    proto = currentProxyData[4].string.lower()
    ip_addr = currentProxyData[0].string
    port = currentProxyData[1].string
    currentRow = '{}  {}  {}'.format(proto, ip_addr, port)
    outFile.write(currentRow + '\n')

outFile.close()
