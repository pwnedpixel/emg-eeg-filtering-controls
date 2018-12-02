import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
import numpy.linalg as linalg
import time
import timeit

#Filters a sampled EEG signal
def filterEEG(time, eeg, low_pass=10, sfreq=200, high_band=15, low_band=30):

    # create bandpass filter for EEG
    high_band = high_band/(1.0*sfreq/2)
    low_band = low_band/(1.0*sfreq/2)
    b, a = sp.signal.butter(4, [high_band,low_band], btype='bandpass')

    #eeg_correctmean = eeg - np.mean(eeg)
    eeg_norm = [i /500.0 for i in eeg]

    eeg_filtered = sp.signal.filtfilt(b, a, eeg_norm)

    eeg_ifft = np.fft.fft(eeg_filtered)
    eeg_real = np.real(eeg_ifft)

    #print eeg_real
    eeg_rectified = abs(eeg_real)

    # low_pass = 1.0*low_pass/(1.0*sfreq)
    # b2, a2 = sp.signal.butter(4, low_pass, btype="lowpass")
    # eeg_envelope = sp.signal.filtfilt(b2,a2, eeg_rectified)

    return eeg_rectified
