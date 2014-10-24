import cookielib
import datetime
import mechanize
import re
from pymongo import MongoClient

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
mc = MongoClient('localhost', 27017)
db = mc.domains
ed = db.expired_domains

domain_re = re.compile(r'href="http://www\.crawlr\.dk/domain/(.*\.dk)"')

def crawl(pageid):
    if pageid == 0:
        url = 'http://www.crawlr.dk/deleted'
    else:
        url = 'http://www.crawlr.dk/deleted/' + str(pageid)
    print url

    page = br.open(url).read()
    domains = domain_re.findall(page)
    return list(set(domains))

br.open('http://www.crawlr.dk/deleted/date/365')

for i in range(0, 100000, 100):
    results = crawl(i)
    for d in results:
        if len(d) <= 6:
            print d
            domain = {'domain': d,
                      'found': datetime.datetime.now()}
            ed.insert(domain)