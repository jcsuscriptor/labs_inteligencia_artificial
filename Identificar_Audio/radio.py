import pyaudio
import wave
import sys
#import resource

chunk = 1024

RATE = 44100
CHANNELS = 2
FORMAT = pyaudio.paInt16
STREAM_URL = 'http://209.8.115.211/7/630/20051/v1/auth.akacast.akamaistream.net/kkrz-fm?akacasthops=1'

import urllib.request


# Content-Type: audio/aacp
f = urllib.request.urlopen(STREAM_URL)

# # Pyaudio stream requires format conversion
# p = pyaudio.PyAudio()
# stream = p.open(format = FORMAT,
#                 channels = CHANNELS,
#                 rate = RATE,
#                 output = True)

# while True:
#     data = f.read(100)
#     stream.write(data)
# stream.close()

# Write raw data
# Note that metadata is included
outfile = open("stream.dump","wb")
while True:
  data = f.read(100)
  outfile.write(data)
  

outfile.close()
p.terminate()