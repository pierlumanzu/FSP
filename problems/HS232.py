import numpy as np
from problems.problem import Problem


class HS232(Problem):

    def __init__(self):
        Problem.__init__(self, 2, np.array((2, 0.5)).reshape(-1, 1))

    def f(self, x: np.array) :
        return float(-(9 - (x[0] - 3) ** 2) * (x[1] ** 3 / np.sqrt(3) / 27))
    
    @property
    def name(self) :
        return "HS232"
