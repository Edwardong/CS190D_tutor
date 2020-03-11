def compute_prob(nTrials, numObserved):
    if nTrials == 0:
        print("invalid number of trials.")
        return
    return numObserved/nTrials