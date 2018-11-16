from copy import deepcopy

from .CDataStats import CDataStats

class CDataStatsNoPreprocess(CDataStats):
    def preprocess(self, x):
        return deepcopy(x)
