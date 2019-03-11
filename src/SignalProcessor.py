from FrameBuffer import FrameBuffer
from filterEMG import filterEMG
import numpy as np
from processIntent import *

class SignalProcessor:
	prevEMG = 0

	def __init__(self):
		self.prevEMG = 0

	def processEMG(self, EMGSample):
		time = time = np.array([i*0.1 for i in range(100)])
		filteredEMG = filterEMG(time, EMGSample, sfreq=100, low_band=49, high_band=10, low_pass=5)
		decision = processIntentEMG(filteredEMG, self.prevEMG)
		prevEMG = decision
		return decision
