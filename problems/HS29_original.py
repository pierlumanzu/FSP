import numpy as np
from problems.HS29 import HS29

from problems.problems_utils.proj_over_convex_set import ProjOverConvexSet


class HS29Original(HS29):

    def __init__(self, c: np.array = None):
        HS29.__init__(self, c)
        self._name = "HS29_Original"
        
        self._proj_op = ProjOverConvexSet(self.g, self.nabla_g, self.nabla2_g)

    def f(self, x: np.array) :
        return float(- x[0] * x[1] * x[2])

    def g(self, x: np.array):
        return np.array(x[0] ** 2 + 2 * x[1] ** 2 + 4 * x[2] ** 2 - 48, dtype=float).reshape(-1, 1)

    def nabla_g(self, x: np.array):
        return np.array((2 * x[0], 4 * x[1], 8 * x[2]), dtype=float).reshape(1, -1)

    def nabla2_g(self, x: np.array):
        ng2 = np.zeros((3, 3, 1), dtype=float)
        ng2[:, :, 0] = np.diag((2., 4., 8.))
        return ng2
