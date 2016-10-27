import re
import download
import urlparse

def link_crawler(seed_url, link_regex) :
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download.download_2(url)
        for link in get_links(html):
            if(re.match(link_regex, link)):
                crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

#link_crawler('http://example.webscraping.com', '/(index|view)')

def link_crawler_2(seed_url, link_regex) :
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download.download_2(url)
        for link in get_links(html):
            if(re.match(link_regex, link)):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


link_crawler_2('http://example.webscraping.com', '/(index|view)')