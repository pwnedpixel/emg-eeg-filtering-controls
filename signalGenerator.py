
import random
import numpy as np

# Generates a signal with three zones, each zone is either high or low
def getSampleOne():

    # for testing purposes, generates random emg signals that are either high or low
    emg = []
    quiet = np.random.uniform(-0.05, 0.05, 25) + 0.08
    burst = np.random.uniform(-1, 1, 25) + 0.08
    for index in range(0, 4):    
        if (random.randint(0,2) == 1):
            emg = np.concatenate([emg, burst])
        else:
            emg = np.concatenate([emg, quiet])
    time = np.array([i*1.0/1000.0 for i in range(0, len(emg), 1)])

    return emg, time

def getSampleTwo():
    emg = []
    size = 0.0
    for index in range(0,25):
        chanceOfBigJump = random.randint(0,5)
        if (random.randint(0,2)==1):
            if (chanceOfBigJump == 0):
                if (size <= 0.5):
                    size = size + 0.5
                else:
                    size = 0.9;
            if (size<1.0):
               size = size + 0.1
        else:
            if (chanceOfBigJump == 0):
                if (size >= 0.5):
                    size = size - 0.5
                else:
                    size = 0.1;
            if (size > 0.0):
                size = size - 0.1 
        signalSection = np.random.uniform(-size, size, 4) + 0.08
        emg = np.concatenate([emg, signalSection])
    time = np.array([i*1.0/1000.0 for i in range(0, len(emg), 1)])

    return emg, time
