# given a filtered EMG signal, determines whether or not the brace should move
def processIntentEMG(filteredSignal, frameBuffer):
    moveThres = 0.08

    # if the mean signal is above moveThres (samples can be 0-1), the brace should move
    if (sum(filteredSignal)/len(filteredSignal) > moveThres):
        return 1
    elif 1 in frameBuffer:
        return 2
    else:
        return 0

# given a filtered EMG signal, determines whether or not the brace should move
def processIntentEEG(filteredSignal, frameBuffer):
    moveThres = 0.05
    #print sum(filteredSignal)/len(filteredSignal)
    if (sum(filteredSignal)/len(filteredSignal) > moveThres):
        return 1
    elif 1 in frameBuffer:
        return 2
    else:
        return 0