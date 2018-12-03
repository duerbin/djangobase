#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 17:00
# @Author  : Aries
# @Site    : 
# @File    : silenceCheck.py
# @Software: PyCharm
#wavpath="../static/test1.wav"
from pydub import AudioSegment
from pydub.utils import audioop
import numpy as np
import wave as we
import math
import matplotlib.pyplot as plt
from io import BytesIO



def detect_leading_silence(sound, silence_threshold=-24.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
     trim_ms += chunk_size

    return trim_ms


def wavread(path):
    wavfile =  we.open(path,"rb")
    params = wavfile.getparams()
    framesra,frameswav= params[2],params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav,dtype = np.short)
    datause.shape = -1,1
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0/framesra)
    return datause,time


def readwavfile(filename, limit=None):
    """
    Reads any file supported by pydub (ffmpeg) and returns the data contained
    within. If file reading fails due to input being a 24-bit wav file,
    wavio is used as a backup.

    Can be optionally limited to a certain amount of seconds from the start
    of the file by specifying the `limit` parameter. This is the amount of
    seconds from the start of the file.

    returns: (channels, samplerate)
    """
    # pydub does not support 24-bit wav files, use wavio when this occurs
    try:

        #audiofile=AudioSegment(data,2,8000,1)
        wavdata,wavtime=wavread(wavpath)

        plt.title("test1.wav")
        plt.subplot(211)
        plt.plot(wavtime,wavdata[0],color='green')
        #buffer = BytesIO()

        #plt.savefig(static,format='png')
        plot_data = buffer.getvalue()
        plt.show()

    except audioop.error:
        fs, _, audiofile = wavio.readwav(filename)

        if limit:
            audiofile = audiofile[:limit * 1000]

        audiofile = audiofile.T
        audiofile = audiofile.astype(np.int16)

        channels = []
        for chn in audiofile:
            channels.append(chn)


def readpcmfile(pcmfile,limit=None):
    """
       Reads any file supported by pydub (ffmpeg) and returns the data contained
       within. If file reading fails due to input being a 24-bit wav file,
       wavio is used as a backup.

       Can be optionally limited to a certain amount of seconds from the start
       of the file by specifying the `limit` parameter. This is the amount of
       seconds from the start of the file.

       returns: (channels, samplerate)
       """
    # pydub does not support 24-bit wav files, use wavio when this occurs


    try:
        fp = open(pcmfile, "rb")
        data=fp.read()
        fp.close()
        #data=np.fromstring(data, np.int16)
        audiofile = AudioSegment(data, sample_width=2, frame_rate=8000, channels=1)
        # audiofile = AudioSegment.from_file(filename)
        start_trim = detect_leading_silence(audiofile)

        if limit:
            audiofile = audiofile[start_trim:limit * 1000]
        else:
            audiofile = audiofile[start_trim:]

        data = np.fromstring(audiofile._data, np.int16)

        filename = pcmfile + ".pcm"
        fp = open(filename, "wb")
        fp.write(data)
        fp.close()
    except audioop.error:
       print( "error")



def getimagefile(wavpath,imgpath):

    wavdata, wavtime = wavread(wavpath)
    plt.axis('off')
    plt.title("test1.wav")
    plt.subplot(211)
    plt.plot(wavtime, wavdata[0], color='green')
    fig = plt.gcf()
    # buffer = BytesIO()
    fig.savefig(imgpath, format='png', transparent=True, dpi=300, pad_inches = 0)


#getimagefile(wavpath)
