# Copyright (c) 2021 Giulio Galvan
# Licensed under the GPL-3.0 License. 
# You may obtain a copy of the License at https://opensource.org/license/gpl-3-0

from typing import Callable


class Counter:

    def __init__(self, fnc: Callable, name: str):
        self.__fnc: Callable = fnc
        self.__lap_count: int = 0
        self.__count: int = 0
        self.__name: str = 'num_{}'.format(name)

    def __call__(self, *args, **kwargs):
        self.__count += 1
        self.__lap_count += 1
        return self.__fnc(*args, **kwargs)

    @property
    def name(self):
        return self.__name

    @property
    def count(self):
        return self.__count

    @property
    def lap(self):
        c = self.__lap_count
        self.__lap_count = 0
        return {self.__name: c}