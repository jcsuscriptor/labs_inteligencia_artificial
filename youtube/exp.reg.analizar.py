#!/usr/bin/python
import re

urlForUserName = "https://www.youtube.com/user/JorgeLuisPeralta"
urlChannel = "https://www.youtube.com/channel/UC-q80GTFK2A0Y6I5ClT-8TQ"

exRegUser = r'https://www.youtube.com/user/(.*)'
exRegChannel = r'https://www.youtube.com/channel/(.*)'

matchUrlUser = re.match( exRegUser, urlForUserName, re.M|re.I)
 
if matchUrlUser:
   print("matchObj.group() : ", matchUrlUser.group())
   print("matchObj.group(1) : ", matchUrlUser.group(1))
else:
   print("No match!!")

matchUrlUser = re.match( exRegUser, urlChannel, re.M|re.I)
if matchUrlUser:
   print("matchObj.group() : ", matchUrlUser.group())
   print("matchObj.group(1) : ", matchUrlUser.group(1))
else:
  print("No match!!")

matchUrlChannel = re.match( exRegChannel, urlForUserName, re.M|re.I)
if matchUrlChannel:
   print("matchObj.group() : ", matchUrlChannel.group())
   print("matchObj.group(1) : ", matchUrlChannel.group(1))
else:
  print("No match!!")

matchUrlChannel = re.match(exRegChannel, urlChannel, re.M|re.I)
if matchUrlChannel:
   print("matchObj.group() : ", matchUrlChannel.group())
   print("matchObj.group(1) : ", matchUrlChannel.group(1))
else:
  print("No match!!")
 

