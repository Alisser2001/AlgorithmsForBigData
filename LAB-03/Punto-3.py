import itertools
import numpy as np

def SparseMatrix3(m=None, **kwargs):

    def add_to_dict(d, key1, key2, val):
        if key1 not in d.keys():
            d[key1] = {}
        d[key1][key2] = val
        return d

    class SparseMatrix3_class:
        def __init__(self, m=m, **kwargs):
            self.rows = {}
            self.shape = (0, 0) if m is None else (len(m), len(m[0]))

            if m is not None:
                for i, row in enumerate(m):
                    for j, val in enumerate(row):
                        if val != 0:
                            add_to_dict(self.rows, i, j, val)

        def to_dense(self):
            r = np.zeros(self.shape)
            for i, row in self.rows.items():
                for j, val in row.items():
                    r[i, j] = val
            return r

        def T(self):
            r = self.__class__(m=None)
            for i, row in self.rows.items():
                for j, val in row.items():
                    add_to_dict(r.rows, j, i, val)
            r.shape = (self.shape[1], self.shape[0])
            return r

    return SparseMatrix3_class(**kwargs)


def random_sparse_matrix(size):
    m = np.random.randint(2, size=size)
    m = m * np.random.randint(10, size=size)
    return m


m = random_sparse_matrix((5, 3))
s = SparseMatrix3(m)

print(m)
