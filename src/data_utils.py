import numpy as np
from pandas import read_csv

def load(filename):
    """
    Loads MNIST from a file and returns it as x, y
    """
    data = np.array(read_csv(filename))
    return (data[:, 1:], data[:, 0])
