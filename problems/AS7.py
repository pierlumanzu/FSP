import numpy as np
from problems.problem import Problem


class AS7(Problem):

    def __init__(self, n: int, c: np.array = None):
        Problem.__init__(self, n, np.ones((n, 1)) * 3, c)
        self._name = "AS7(n={})".format(n)

    def f(self, x: np.array):
        return float(np.sum((x.flatten()) ** 2))
