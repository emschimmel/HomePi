try:
    # Python 3 imports
    from urllib import request as Request
    from urllib.request import urlopen as urlopen
    from urllib.parse import quote
    from urllib.parse import urlencode as urlencode
    from urllib.error import URLError
    # needed for code to work on Python3
    xrange = range
    unicode = str
except ImportError:
    # Python 2 imports
    from urllib2 import Request as Request
    from urllib2 import urlopen as urlopen
    from urllib import quote
    from urllib import urlencode as urlencode
    from urllib2 import URLError

#--------------------------------------------------------
# http://www.voidspace.org.uk/python/articles/urllib2.shtml#headers
#--------------------------------------------------------
class httpConnectWithOauth:

    def __init__(self):
        self.accestoken = False

    def getAcces(self, url, apikey):
        values = {'client_id=' : apikey}

        data = urlencode(values)
        req = Request(url+"?response_type=code&redirect_uri=localhome&client_id="+apikey)
        response = urlopen(req)
        the_response = response.read()
        print("---->", the_response)
        self.accestoken = the_response

    def getWithValues(self, url, apikey, device=False):
        values = {'client_id=' : apikey}
        data = urlencode(values)
        req = Request(url, data)
        response = urlopen(req)
        the_response = response.read()
        print("---->", the_response)
        return the_response
