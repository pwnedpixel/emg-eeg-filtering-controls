import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
import time
import timeit

#Filters a sampled EMG signal
def filterEMG(time, emg, low_pass=20, sfreq=1000, high_band=20, low_band=450):

    # create bandpass filter for EMG
    high_band = high_band/(1.0*sfreq/2)
    low_band = low_band/(1.0*sfreq/2)
    b, a = sp.signal.butter(4, [high_band,low_band], btype='bandpass')

    emg_correctmean = emg - np.mean(emg)

    emg_filtered = sp.signal.filtfilt(b, a, emg_correctmean)
    emg_rectified = abs(emg_filtered)

    low_pass = 1.0*low_pass/(1.0*sfreq)
    b2, a2 = sp.signal.butter(4, low_pass, btype="lowpass")
    emg_envelope = sp.signal.filtfilt(b2,a2, emg_rectified)

    return emg_envelope

















# currentTime = time.strftime("%Y%m%d-%H%M%S")

# burst1 = np.random.uniform(-1, 1, 1000) + 0.08
# burst2 = np.random.uniform(-1, 1, 1000) + 0.08
# quiet = np.random.uniform(-0.05, 0.05, 500) + 0.08
# emg = np.concatenate([quiet, burst1, quiet, burst2, quiet])
# timeit.timeit('filteremg(time, emg, sfreq=1000, low_pass=20)', number=10000)

# time = np.array([i*1.0/1000 for i in range(0, len(emg), 1)])

# # Plot the emg signal and save the image
# fig = plt.figure()
# plt.subplot(1,2,1)
# plt.subplot(1,2,1).set_title("Input signal")
# plt.plot(time, emg)
# plt.locator_params(axis='x', nbins=4)
# plt.locator_params(axis='y', nbins=4)
# plt.ylim(-1.5, 1.5)
# plt.xlabel("Time (sec)")
# plt.ylabel("EMG (a.u.)")
# fig_name = "input-"+currentTime+".png"
# fig.set_size_inches(w=11,h=7)
# fig.savefig(fig_name)

# Filter and save output
# get the mean
# emg_correctmean = emg - np.mean(emg)

# filteremg(time, emg_correctmean, low_pass=5)