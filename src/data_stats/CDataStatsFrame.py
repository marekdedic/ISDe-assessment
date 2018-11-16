from copy import deepcopy

from .CDataStats import CDataStats

class CDataStatsFrame(CDataStats):
    def __init__(self, w, h, frame_size, bins = list(range(256))):
        super().__init__(bins)
        self.w = w
        self.h = h
        self.frame_size = frame_size

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, w):
        self._w = w

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    @property
    def frame_size(self):
        return self._frame_size

    @frame_size.setter
    def frame_size(self, frame_size):
        self._frame_size = frame_size

    def preprocess(self, x):
        xp = deepcopy(x).reshape(self.h, self.w)
        return xp[self.frame_size:xp.shape[0] - self.frame_size, self.frame_size:xp.shape[1] - self.frame_size].ravel();
