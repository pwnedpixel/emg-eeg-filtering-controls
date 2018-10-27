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
import cv2

class FrameBuffer(object):
    frameBuffer = np.zeros(3)

    @staticmethod
    def getBuffer():
        return FrameBuffer.frameBuffer

    @staticmethod
    def addElement(x):
        FrameBuffer.frameBuffer = np.concatenate([[x], FrameBuffer.frameBuffer[:-1]])

fig = plt.figure(figsize=(12,6))

# Updates the current frame. process a new section of samples and displays them
def update(frame):

    # for testing purposes, generates random emg signals that are either high or low
    emg, time = getSampleTwo()

    # filters the generate signal
    filteredEMG = filterEMG(time, emg)

    plt.subplot(1,3,1)
    plt.ylim(-1.5, 1.5)
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
ani = FuncAnimation(fig, update, blit=True, interval=100, save_count=50)

plt.show()
