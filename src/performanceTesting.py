import numpy as np
import timeit
from filterEMG import filterEMG
import random
import timeit
from signalGenerator import *

# timing test for the filterEMG function
print timeit.timeit('filterEMG(time, emg)','from signalGenerator import getSampleTwo; from filterEMG import filterEMG; emg, time = getSampleTwo()', number=500)