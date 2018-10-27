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
# interactive(True)



fig = plt.figure(figsize=(12,6))    

def update(frame):
    emg = []
    quiet = np.random.uniform(-0.05, 0.05, 100) + 0.08
    burst = np.random.uniform(-1, 1, 100) + 0.08
    for index in range(0, 3):    
        if (random.randint(0,2) == 1):
            emg = np.concatenate([emg, burst])
        else:
            emg = np.concatenate([emg, quiet])
    time = np.array([i*1.0/1000.0 for i in range(0, len(emg), 1)])
    filteredEMG = filterEMG(time, emg)

    plt.subplot(1,3,1)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('Time (sec)')
    plt.ylabel('EMG (a.u.)')
    imOrig=plt.plot(time, emg, animated=True, color="blue")
    
    
    plt.subplot(1,3,2)
    imFilt=plt.plot(time, filteredEMG, animated=True, color="blue")
    

    plt.subplot(1,3,3)

    if (processIntent(filteredEMG)  == 1):
        # im2=plt.plot(time, np.zeros(len(time)), animated=True)
        img=mpimg.imread('green.png')
        # img = cv2.imread("red.png")
        imgColour=plt.imshow(img)
        # im2 = plt.plot(img[2], animated=True)
    else:
        img=mpimg.imread('red.png')
        # img = cv2.imread("red.png")
        imgColour=plt.imshow(img)
        # im2 = plt.plot(img[2], animated=True)
        
        # im2 = plt.plot(np.array([1,2]),np.array([255,255]), animated=True)
    return tuple(imOrig) + tuple(imFilt) + (imgColour,)

# emg = np.random.uniform(-0.05, 0.05, 300) + 0.08

ani = FuncAnimation(fig, update, blit=True, interval=300)

plt.show()

# while True:
    
#     # plt.clf()
#     # plt.subplot(1,2,1)
#     # plt.subplot(1,2,1).set_title("Input signal")
#     # plt.plot(time, emg, animated=True)
#     # plt.locator_params(axis='x', nbins=4)
#     # plt.locator_params(axis='y', nbins=4)
#     # plt.ylim(-1.5, 1.5)
#     # plt.xlabel("Time (sec)")
#     # plt.ylabel("EMG (a.u.)")

#     # plt.subplot(1,2,2)
#     # plt.subplot(1,2,2).set_title("Output signal")
    
#     # plt.plot(time, filteremg(time, emg, sfreq=1000, low_pass=20), animated=True)
#     # plt.locator_params(axis='x', nbins=4)
#     # plt.locator_params(axis='y', nbins=4)
    
#     # fig.tight_layout()
    
#     # fig_name=str(index) + ".png"
#     # fig.set_size_inches(w=11, h=7)
#     # fig.savefig(fig_name)
#     # plt.close('all')
#     # print "Created block " + str(index)

# raw_input("press enter")
# plt.close('all')