#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

import configuration

if __name__ == '__main__':
    

     
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(configuration.config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    print(re.recognize_by_file(sys.argv[1], 0, 10))

    print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file(sys.argv[1])))

    buf = open(sys.argv[1], 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    print(re.recognize_by_filebuffer(buf, 0, 10))

