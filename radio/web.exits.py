
#httplib
#You are running Python 2 code on Python 3. In Python 3, the module has been renamed to http.client.

import httplib
c = httplib.HTTPConnection('www.example.com')
c.request("HEAD", '')
if c.getresponse().status == 200:
   print('web site exists')