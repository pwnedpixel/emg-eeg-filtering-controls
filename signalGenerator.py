import numpy as np
import matplotlib.pyplot as plt
from filterEMG import filterEMG 
from processIntent import processIntent
import random
from matplotlib import interactive
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
import time as tm
import timeit
from PIL import Image, ImageDraw
import cv2

fig = plt.figure(figsize=(12,6))    

# Updates the current frame. process a new section of samples and displays them
def update(frame):

    # for testing purposes, generates random emg signals that are either high or low
    emg = []
    quiet = np.random.uniform(-0.05, 0.05, 100) + 0.08
    burst = np.random.uniform(-1, 1, 100) + 0.08
    for index in range(0, 3):    
        if (random.randint(0,2) == 1):
            emg = np.concatenate([emg, burst])
        else:
            emg = np.concatenate([emg, quiet])
    time = np.array([i*1.0/1000.0 for i in range(0, len(emg), 1)])

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
    if (processIntent(filteredEMG)  == 1):
        img=mpimg.imread('green.png')
        imgColour=plt.imshow(img)
    else:
        img=mpimg.imread('red.png')
        imgColour=plt.imshow(img)
        
    return tuple(imOrig) + tuple(imFilt) + (imgColour,)

# Animate the graphs
ani = FuncAnimation(fig, update, blit=True, interval=300)

plt.show()
