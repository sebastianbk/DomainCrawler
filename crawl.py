import cookielib
import mechanize
import re

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

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
        if len(d) <= 5:
            print d