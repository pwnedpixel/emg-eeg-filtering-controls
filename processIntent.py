# given a filtered EMG signal, determines whether or not the brace should move
def processIntent(filteredSignal):
    if (sum(filteredSignal)/len(filteredSignal) > 0.25):
        return 1
    else:
        return 0