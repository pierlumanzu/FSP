import numpy as np
from problems.problem import Problem


class AS6(Problem):

    def __init__(self, n: int, c: np.array = None):
        Problem.__init__(self, n, np.zeros((n, 1)), c)
        self._name = "AS6(n={})".format(n)

    def f(self, x: np.array):
        return float(np.sum((x.flatten() - 1) ** 2))
