import numpy as np
from problems.problem import Problem


class HS22(Problem):

    def __init__(self):
        Problem.__init__(self, 2, np.array((2., 2.)).reshape(-1, 1))

    def f(self, x: np.array) :
        return float((x[0] - 2) ** 2 + (x[1] - 1) ** 2)

    @property
    def name(self) :
        return "HS22"
