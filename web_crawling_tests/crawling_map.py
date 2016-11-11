import download
import re
import itertools

def crawl_sitemap(url):
    #download the sitemap file
    sitemap = download.download_2(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download.download_2(link)

print('Hello World')
#crawl_sitemap('http://example.webscraping.com/sitemap.xml')

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download.download_2(url)
    if html is None:
        break
    else:
        pass

max_errors = 5
num_errors = 0

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download.download_2(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0