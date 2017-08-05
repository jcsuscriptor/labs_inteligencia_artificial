#!/usr/bin/python
import re

url = "https://www.facebook.com/norkamusica/?fref=ts"
url2 = "https://www.facebook.com/kalethoficial/"
url3 = "https://www.facebook.com/kalethoficial"


exRegFacebook = r'https://www.facebook.com/(.*)/.*|https://www.facebook.com/(.*)'

 
match  = re.match( exRegFacebook, url, re.M|re.I)

if match:
   print("match url!!")
   print("matchObj.group() : ", match.group())
   print("matchObj.group(1) : ", match.group(1))
   print("matchObj.group(2) : ", match.group(2))
else:
   print("No match url!!")
 

match  = re.match( exRegFacebook, url2, re.M|re.I)

if match:
   print("match url2!!")
   print("matchObj.group() : ", match.group())
   print("matchObj.group(1) : ", match.group(1))
   print("matchObj.group(2) : ", match.group(2))
else:
   print("No match url2!!")
  

match  = re.match( exRegFacebook, url3, re.M|re.I)

if match:
   print("match url3!!")
   print("matchObj.group() : ", match.group())
   print("matchObj.group(1) : ", match.group(1))
   print("matchObj.group(2) : ", match.group(2))
else:
   print("No match url3!!")  