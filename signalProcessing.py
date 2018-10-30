import numpy as np
import matplotlib.pyplot as plt
from filterEMG import filterEMG 
from processIntent import processIntent
from signalGenerator import *
import random
from matplotlib import interactive
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
import time as tm
import timeit
from PIL import Image, ImageDraw
import mne

class FrameBuffer(object):
    frameBuffer = np.zeros(2)
    emgFromFile = []
    timeFromFile = []
    currentIndex = 0

    @staticmethod
    def getBuffer():
        return FrameBuffer.frameBuffer

    @staticmethod
    def addElement(x):
        FrameBuffer.frameBuffer = np.concatenate([[x], FrameBuffer.frameBuffer[:-1]])
    
    @staticmethod
    def loadData():
        FrameBuffer.emgFromFile, FrameBuffer.timeFromFile = getRealSample()
    
    @staticmethod
    def getNextSample():
        emg = FrameBuffer.emgFromFile[0:200]
        FrameBuffer.emgFromFile = np.concatenate([FrameBuffer.emgFromFile[200:],FrameBuffer.emgFromFile[0:200]])
        time = np.array([i*1.0/200.0 for i in range(0, len(emg), 1)])

        return np.array(emg).astype(np.float), time

fig = plt.figure(figsize=(12,6))

# Updates the current frame. process a new section of samples and displays them
def update(frame):

    # for testing purposes, generates random emg signals that are either high or low
    emg, time = FrameBuffer.getNextSample()

    # filters the generate signal
    filteredEMG = filterEMG(time, emg)

    plt.subplot(1,3,1)
    plt.ylim(-500, 500)
    plt.xlabel('Time (sec)')
    plt.ylabel('EMG (a.u.)')

    # plot the generated signal in the first plot
    imOrig=plt.plot(time, emg, animated=True, color="blue")
    
    plt.subplot(1,3,2)
    # plot the filtered signal in the second plot
    imFilt=plt.plot(time, filteredEMG, animated=True, color="blue")

    plt.subplot(1,3,3)
    # uses the processIntent function to determine if the brace should move for the
    #   current time frame, displays green if it should move, red if not

    decision = processIntent(filteredEMG, FrameBuffer.getBuffer())
    if decision == 1:
        FrameBuffer.addElement(1)
        img=mpimg.imread('green.png')
        imgColour=plt.imshow(img)
    elif decision == 2:
        FrameBuffer.addElement(0)
        img=mpimg.imread('green.png')
        imgColour=plt.imshow(img)
    else:
        FrameBuffer.addElement(0)
        img=mpimg.imread('red.png')
        imgColour=plt.imshow(img) 

    return tuple(imOrig) + tuple(imFilt) + (imgColour,)

# Animate the graphs
FrameBuffer.loadData()
ani = FuncAnimation(fig, update, blit=True, interval=200, save_count=50)
# raw = mne.io.read_raw_edf("S001R04.edf", preload=True)
# raw.set_eeg_reference("average", projection=False)
# events = mne.find_events(raw)
# plt.plot(raw._data[-1])
# events = mne.find_events(raw, initial_event=True)  # requires MNE 0.16
# print events

# print DataLoader.dataPoints

plt.show()
