import numpy as np
from problems.problem import Problem


class HS43(Problem):

    def __init__(self):
        Problem.__init__(self, 4, np.zeros((4, 1), dtype=float))

    def f(self, x: np.array):
        return float(x[0] ** 2 + x[1] ** 2 + 2 * x[2] ** 2 + x[3] ** 2 - 5 * x[0] - 5 * x[1] - 21 * x[2] + 7 * x[3])

    @property
    def name(self) :
        return "HS43"
