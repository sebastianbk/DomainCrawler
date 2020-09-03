import cookielib
import datetime
import mechanize
import re
from pymongo import MongoClient

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
mc = MongoClient('localhost', 27017)
db = mc.domains
ed = db.expired_domains

domain_re = re.compile(r'href="/domain/(.*\.dk)"')

def crawl(pageid):
    url = 'http://www.crawlr.dk/deleted/?range=365&page=' + str(pageid)
    print url

    page = br.open(url).read()
    domains = domain_re.findall(page)
    return list(set(domains))

br.open('https://www.crawlr.dk/deleted/?range=365')

for i in range(1, 100000):
    results = crawl(i)
    for d in results:
        if len(d) <= 6:
            print d
            domain = {'domain': d,
                      'found': datetime.datetime.now()}
            ed.insert(domain)