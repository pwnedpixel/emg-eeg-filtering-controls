# given a filtered EMG signal, determines whether or not the brace should move
def processIntent(filteredSignal):
    moveThres = 0.25

    # if the mean signal is above moveThres (samples can be 0-1), the brace should move
    if (sum(filteredSignal)/len(filteredSignal) > moveThres):
        return 1
    else:
        return 0