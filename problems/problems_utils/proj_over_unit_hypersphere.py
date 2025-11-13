import numpy as np


class ProjOverUnitHypersphere:

    def __init__(self, n, c=None):
        self.__c = c * np.ones((n, 1)) if c is not None else np.zeros((n, 1))

    def __call__(self, x: np.ndarray):
        if np.linalg.norm(x - self.__c)**2 > 1:
            return self.__c + (x - self.__c) / np.linalg.norm(x - self.__c), True
        else:
            return x, False
