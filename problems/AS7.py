import numpy as np
from problems.problem import Problem


class AS7(Problem):

    def __init__(self, n: int):
        Problem.__init__(self, n, np.ones((n, 1)) * 3)

    def f(self, x: np.array):
        return float(np.sum((x.flatten()) ** 2))
    
    @property
    def name(self) :
        return "AS7(n={})".format(self._n)
