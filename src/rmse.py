import numpy as np


def rms(actual, prediction):
    rms = np.sqrt(np.mean(np.power((np.array(actual)-np.array(prediction)), 2)))
    return rms
