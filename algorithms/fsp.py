from typing import Callable, Union, Tuple
from time import time
import numpy as np

from algorithms.algorithms_utils.history import History
from algorithms.algorithms_utils.counter import Counter


class FSP:

    def __init__(self, max_it: int = -1, max_nf: int = -1, verbosity: bool = False,
                 min_alpha: float = 1e-6, delta: float = 0.5, sigma: float = 1e-5):
        self.__max_it = max_it
        self.__max_nf = max_nf
        self.__verbosity = verbosity
        self.__min_alpha = min_alpha
        self.__delta = delta
        self.__sigma = sigma

    def solve(self, f: Callable[[np.ndarray], float], proj_op: Callable[[np.ndarray], np.ndarray], x0: Union[None, np.ndarray]):

        f = Counter(f, name='f')
        n_proj = 0
        tilde_alpha = 1
        history = History()
        B = np.concatenate((np.eye(len(x0)), -np.eye(len(x0))), axis=0)
        it = 0
        stop = False
        resume_idx_d = 0

        x, is_nontrivial_proj = proj_op(np.copy(x0))
        x = x.flatten()
        n_proj += is_nontrivial_proj
        fx = f(x[:, np.newaxis]) 

        while not stop:
            t0 = time()

            success = False

            for idx_d in range(len(B)):
                x_new, is_nontrivial_proj = proj_op((x + tilde_alpha * B[(idx_d + resume_idx_d) % len(B)])[:, np.newaxis])
                x_new = x_new.flatten()
                n_proj += is_nontrivial_proj
                f_new = f(x_new[:, np.newaxis])
                
                if f_new < fx - self.__sigma * tilde_alpha**2:
                    x = np.copy(x_new)
                    fx = f_new
                    tilde_alpha = max(1e-6, tilde_alpha / 0.99)
                    resume_idx_d = (idx_d + resume_idx_d + 1) % len(B)
                    success = True
                    break

            if not success:
                tilde_alpha *= self.__delta

            it += 1
            stop = self.__check_stopping_crit(it, f.count, tilde_alpha)
            elapsed_time = time() - t0
                
            history.add_iterate({'x': x[:, np.newaxis].copy()})
            history.update(
                {'f': fx, 'alpha_max': tilde_alpha, 'time': elapsed_time, 'n_proj': n_proj},
                f.lap
            )

            if self.__verbosity:
                history.print_last()

        return x[:, np.newaxis], history

    def __check_stopping_crit(self, it: int, nf: int, tilde_alpha: float):
        return (0 < self.__max_it <= it) or tilde_alpha <= self.__min_alpha or (0 < self.__max_nf <= nf)
        
    def __repr__(self):
        return "FSP"

    def __str__(self):
        return self.__repr__()
