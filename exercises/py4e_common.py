import urllib.request


def configure_proxies():
    proxies = {'http': 'http://user:password@webproxy-se.corp.vattenfall.com:8080',
               'https': 'http://user:password@webproxy-se.corp.vattenfall.com:8080'}
    proxy = urllib.request.ProxyHandler(proxies)
    auth = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
