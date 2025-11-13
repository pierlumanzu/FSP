import numpy as np
from problems.problem import Problem


class HS65(Problem):

    def __init__(self, c: np.array = None):
        Problem.__init__(self, 3, np.array((-5, 5, 0), dtype=float).reshape(-1, 1), c)
        self._name = "HS65"

    def f(self, x: np.array):
        return float((x[0] - x[1]) ** 2 + ((x[0] + x[1] - 10) ** 2) / 9 + (x[2] - 5) ** 2)
