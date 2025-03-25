import numpy as np
from problems.problem import Problem


class HS29(Problem):

    def __init__(self):
        Problem.__init__(self, 3, np.array((1., 1., 1.)).reshape(-1, 1))

    def f(self, x: np.array) :
        return float(- x[0] * x[1] * x[2])

    @property
    def name(self) :
        return "HS29"
