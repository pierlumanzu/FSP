# Copyright (c) 2021 Giulio Galvan
# Licensed under the GPL-3.0 License. 
# You may obtain a copy of the License at https://opensource.org/license/gpl-3-0

from _warnings import warn
import numpy as np
from cvxopt import matrix, solvers
from cvxopt.solvers import cp
from typing import Callable
import cvxopt

cvxopt.solvers.options['show_progress'] = False
solvers.options['abstol'] = 1e-17
solvers.options['reltol'] = 1e-17


class ProjOverConvexSet:

    def __init__(self, 
                 g: Callable[[np.ndarray], np.ndarray], 
                 nabla_g: Callable[[np.ndarray], np.ndarray], 
                 nabla2_g: Callable[[np.ndarray], np.ndarray]):
        self.__g = g
        self.__nabla_g = nabla_g
        self.__nabla2_g = nabla2_g

        self.__m, self.__n = None, None

    def __F(self, y, x=None, z=None):
        if self.__m is None:
            t = self.__nabla_g(y)
            self.__n = t.shape[1]
            self.__m = t.shape[0]

        if x is None:
            x0 = matrix(y.reshape((-1, 1)))
            return self.__m, x0
        else:
            x = np.array(x)
            f = np.array((0.5 * np.linalg.norm(y - x) ** 2,))
            f = np.vstack((f, self.__g(x).reshape(-1, 1)))
            Df = np.array(x - y).reshape(-1, 1).T
            # ng = self.__nabla_g(x)
            Df = np.vstack((Df, self.__nabla_g(x)))
            f, Df, = matrix(f), matrix(Df)
            if z is None:
                return f, Df
            else:
                H = np.eye(self.__n).reshape(self.__n, self.__n, 1)
                # ng2 = self.__nabla2_g(x)
                H = np.concatenate((H, self.__nabla2_g(x)), axis=2)
                H = H.dot(z).squeeze()
                return f, Df, matrix(H)

    def __call__(self, x: np.ndarray):
        sol = cp(F=lambda x_=None, z_=None: self.__F(x, x_, z_))
        
        status = sol['status']
        if status != 'optimal':
            warn('Non optimal solution returned by the solver for proj op')
       
        return np.array(sol['x']).reshape(-1, 1), np.any(self.__g(x) > 0)
