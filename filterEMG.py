import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
import numpy.linalg as linalg
import time
import timeit

#Filters a sampled EMG signal
def filterEMG(time, emg, low_pass=10, sfreq=200, high_band=20, low_band=99):

    # create bandpass filter for EMG
    high_band = high_band/(1.0*sfreq/2)
    low_band = low_band/(1.0*sfreq/2)
    b, a = sp.signal.butter(4, [high_band,low_band], btype='bandpass')

    emg_correctmean = emg - np.mean(emg)
    emg_norm = [i /500.0 for i in emg_correctmean]

    emg_filtered = sp.signal.filtfilt(b, a, emg_norm)
    emg_rectified = abs(emg_filtered)

    low_pass = 1.0*low_pass/(1.0*sfreq)
    b2, a2 = sp.signal.butter(4, low_pass, btype="lowpass")
    emg_envelope = sp.signal.filtfilt(b2,a2, emg_rectified)

    return emg_envelope
