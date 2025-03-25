# Copyright (c) 2021 Giulio Galvan
# Licensed under the GPL-3.0 License. 
# You may obtain a copy of the License at https://opensource.org/license/gpl-3-0

import pandas as pd
import numpy as np


class History:
    float_deafault_fmt = ":.3e"

    def __init__(self):
        self.__records: dict = {}
        self.__num_it: int = 0
        self.__formats: dict = {}
        self.__iterates: dict = {}
        self.__num_iterates: int = 0

    def update(self, *record: dict):
        for r in record:
            for key, value in r.items():
                if key not in self.__records:
                    self.__records[key] = [np.nan] * self.__num_it
                self.__records[key].append(r[key])

        self.__num_it += 1

    def add_iterate(self, *record: dict):
        for r in record:
            for key, value in r.items():
                if key not in self.__iterates:
                    self.__iterates[key] = [np.nan] * self.__num_iterates
                self.__iterates[key].append(r[key])

        self.__num_iterates += 1

    def set_formats(self, formats: dict):
        self.__formats.update(formats)

    def print_last(self):
        for key in self.__records.keys():
            if key not in self.__formats:
                self.__formats[key] = History.float_deafault_fmt if type(self.__records[key][0]) in [float] else ""

        s = "it: {} -> ".format(self.__num_it) + ", ".join(
            [("{}: {" + self.__formats[key] + "}").format(key, value[-1]) for key, value in self.__records.items()])
        print(s)

    @property
    def dataframe(self):
        df = pd.DataFrame(self.__records)
        df['it'] = np.arange(self.__num_it)
        df.set_index('it', inplace=True)
        return df

    @property
    def iterates(self):
        return self.__iterates
