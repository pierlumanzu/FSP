import numpy as np
from abc import ABC, abstractmethod

from problems.problems_utils.proj_over_unit_hypersphere import ProjOverUnitHypersphere


class Problem(ABC):

    def __init__(self, n, x0):
        self._n = n
        self._x0 = x0

        self._proj_op = ProjOverUnitHypersphere()

    @abstractmethod
    def f(self, x: np.array):
        pass

    def g(self, x: np.array):
        x = x.flatten()
        return np.array(np.sum([x[i]**2 for i in range(self._n)]) - 1, dtype=float).reshape(-1, 1)

    def nabla_g(self, x: np.array):
        pass

    def nabla2_g(self, x: np.array):
        pass

    def proj_op(self, x: np.array):
        return self._proj_op(x)

    @property
    def x0(self):
        return self._x0

    @property
    @abstractmethod
    def name(self) :
        """:returns the name of the problem"""

    def __repr__(self):
        return self.name
