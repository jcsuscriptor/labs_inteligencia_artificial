
#import httplib
#You are running Python 2 code on Python 3. In Python 3, the module has been renamed to http.client.
#https://stackoverflow.com/questions/13778252/import-httplib-importerror-no-module-named-httplib

import http.client

#"

c = http.client.HTTPConnection('www.example.com')
c.request("HEAD", '')
if c.getresponse().status == 200:
   print('web site exists')

'''
d =  http.client.HTTPSConnection("https://t.co/Ul05tjMCZy")   
d.request("HEAD", '')
if d.getresponse().status == 200:
   print('web site exists.https')
'''

d =  http.client.HTTPSConnection("www.t.co/Ul05tjMCZy")   
d.request("HEAD", '')
if d.getresponse().status == 200:
   print('web site exists.https')