import numpy as np


class ProjOverUnitHypersphere:

    def __call__(self, x: np.ndarray):
        if np.linalg.norm(x)**2 > 1:
            return x / np.linalg.norm(x), True
        else:
            return x, False
