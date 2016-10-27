import urllib2

def download(url):
    return urllib2.urlopen(url).read()

def download_2(url):
    print 'Downloading... : ', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error : ', e.reason
        html = None
    return html

def download_3(url, num_retries = 2):
    print 'Downloading... : ', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error : ', e.reason
        html = None
        if num_retries > 0 :
            if hasattr(e, 'code') and 500 <= e.code <= 600 :
                return download_3(url, num_retries - 1)
    return html

def download_4(url, user_agent='wswp', num_retries = 2):
    print 'Downloading... : ', url
    headers = {'User-agent' : user_agent}
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error : ', e.reason
        html = None
        if num_retries > 0 :
            if hasattr(e, 'code') and 500 <= e.code <= 600 :
                return download_3(url, num_retries - 1)
    return html

#print 'Hello World'
#download_2('http://httpstat.us/500')
#download_3('http://httpstat.us/500')