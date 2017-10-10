from urllib.parse import urlparse
import re

url = 'www.radiocatolicacuenca.com.ec'
o = urlparse(url)

print(url)
print(o)
print()

url = 'http://www.radiocatolicacuenca.com.ec'
o = urlparse(url)

print(url)
print(o)
print()

url = 'http://www.radiocatolicacuenca.com.ec/pagina.html'
o = urlparse(url)

print(url)
print(o)
print()

url = 'https://www.radiocatolicacuenca.com.ec'
o = urlparse(url)

print(url)
print(o)
print()

url = 'radiocatolicacuenca.com.ec'
o = urlparse(url)

print(url)
print(o)
print()

url = 'radiocatolicacuenca.com.ec/pagina.html'
o = urlparse(url)

print(url)
print(o)
print()

url = 'radiocatolicacuenca.com.ec/pagina.html'
o = urlparse(url, 'http')
print(url)
print(o)
print()


exReg = r'http://(.+)|www\.(.+)|https://(.+)|(.+\.*)'

#https://stackoverflow.com/questions/6344993/problems-parsing-an-url-with-python
exReg2 = r'(?:http|https)://'

url = 'radiocatolicacuenca.com.ec/pagina.html'
match  = re.match( exReg, url, re.M|re.I)
if match:
    print(match)
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4)) 

url = 'http://radiocatolicacuenca.com.ec/pagina.html'
match  = re.match( exReg2, url, re.M|re.I)
if match:
    print(match)
else:
    print('no match')  

url = 'radiocatolicacuenca.com.ec/pagina.html'
match  = re.match( exReg2, url, re.M|re.I)
if match:
    print(match)     
else:
    print('no match')    