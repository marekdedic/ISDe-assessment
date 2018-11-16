from abc import ABC, abstractmethod
from matplotlib import pyplot
import numpy as np

class CDataStats(ABC):
    def __init__(self, bins = list(range(256))):
        self.bins = bins

    @property
    def bins(self):
        return self._bins

    @bins.setter
    def bins(self, bins):
        self._bins = bins

    @abstractmethod
    def preprocess(self, x):
        pass

    def mean(self, x):
        return np.mean(self.preprocess(x))

    def histogram(self, x):
        print(self.bins)
        pyplot.hist(self.preprocess(x), bins = self.bins)
        pyplot.xlabel('Pixel value')
        pyplot.ylabel('Frequency')

    def dataset_mean(self, ds):
        return np.mean([self.mean(x) for x in ds])
