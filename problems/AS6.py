import numpy as np
from problems.problem import Problem


class AS6(Problem):

    def __init__(self, n: int):
        Problem.__init__(self, n, np.zeros((n, 1)))

    def f(self, x: np.array):
        return float(np.sum((x.flatten() - 1) ** 2))
    
    @property
    def name(self):
        return "AS6(n={})".format(self._n)

