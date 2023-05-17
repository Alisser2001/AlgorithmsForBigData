import itertools
import numpy as np


def SparseMatrix2(m=None, **kwargs):

    def add_to_dict(d, key1, key2, val):
        if key1 not in d.keys():
            d[key1] = {}
        d[key1][key2] = val
        return d

    class SparseMatrix2_class:

        def __init__(self, m=m, **kwargs):
            self.rows = {}
            self.shape = (0, 0) if m is None else (len(m), len(m[0]))

            if m is not None:
                for i, row in enumerate(m):
                    for j, val in enumerate(row):
                        if val != 0:
                            add_to_dict(self.rows, i, j, val)

        def sparseness_metric(self):
            metric = self.shape[0] * self.shape[1]
            non_zero_elements = sum(len(row) for row in self.rows.values())
            sparseness = 1 - (non_zero_elements / metric)
            return sparseness

    return SparseMatrix2_class(**kwargs)


def random_sparse_matrix(size):
    m = np.random.randint(2, size=size)
    m = m * np.random.randint(10, size=size)
    return m


m = random_sparse_matrix((5, 3))

sm = SparseMatrix2(m)
print(m.shape, sm.sparseness_metric())

s = SparseMatrix2(m)
print("rows", s.rows)
print("length of each row", [len(s.rows[i]) for i in list(s.rows.keys())])

s = SparseMatrix2(None)
s.shape
