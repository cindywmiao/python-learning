__author__ = 'miaowang'

import robotparser

html = 'http://example.webscraping.com/robots.txt'
rp = robotparser.RobotFileParser()
rp.set_url(html)
rp.read()
url = 'http://example.webscraping.com/'
user_agent = 'BadCrawler'
print rp.can_fetch(user_agent, url)
user_agent = 'GoodCrawler'
print rp.can_fetch(user_agent, url)

