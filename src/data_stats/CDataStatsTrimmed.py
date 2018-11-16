from copy import deepcopy

from .CDataStats import CDataStats

class CDataStatsTrimmed(CDataStats):
    def __init__(self, k, bins = list(range(256))):
        super().__init__(bins)
        self.k = k

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, k):
        self._k = k

    def preprocess(self, x):
        xp = deepcopy(x)
        xp.sort()
        return xp[self.k:xp.shape[0] - self.k];
