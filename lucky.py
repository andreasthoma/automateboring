#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Searching...') # display text while downloading Google pages.
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#: Retrieve top search results links.

soup = bs4.BeautifulSoup(res.text)

#: Open individual top search results in new tabs.

linkElems = soup.select('.r a')
numOpen = min(3, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
