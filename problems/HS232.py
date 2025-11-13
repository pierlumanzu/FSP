import numpy as np
from problems.problem import Problem


class HS232(Problem):

    def __init__(self, c: np.array = None):
        Problem.__init__(self, 2, np.array((2, 0.5)).reshape(-1, 1), c)
        self._name = "HS232"

    def f(self, x: np.array):
        return float(-(9 - (x[0] - 3) ** 2) * (x[1] ** 3 / np.sqrt(3) / 27))