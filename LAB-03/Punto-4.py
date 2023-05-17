import itertools
import numpy as np


def SparseMatrix4(m=None, **kwargs):

    def add_to_dict(d, key1, key2, val):
        if key1 not in d.keys():
            d[key1] = {}
        d[key1][key2] = val
        return d

    class SparseMatrix4_class:
        def __init__(self, m=m, **kwargs):
            self.rows = {}
            self.shape = (0, 0) if m is None else (len(m), len(m[0]))

            if m is not None:
                for i, row in enumerate(m):
                    for j, val in enumerate(row):
                        if val != 0:
                            add_to_dict(self.rows, i, j, val)

        def __getitem__(self, pos):
            i, j = pos
            assert 0 <= i < self.shape[0] and 0 <= j < self.shape[1], "Index out of range"
            if i in self.rows and j in self.rows[i]:
                return self.rows[i][j]
            else:
                return 0

    return SparseMatrix4_class(**kwargs)


def random_sparse_matrix(size):
    m = np.random.randint(2, size=size)
    m = m * np.random.randint(10, size=size)
    return m


m = random_sparse_matrix((5, 3))

print("original matrix shape", m.shape)
print(m)


s = SparseMatrix4(m)

print("inner dict", s.rows)
print("\ncoord   value_in_m       value_in_s")
for i, j in itertools.product(list(range(m.shape[0])), list(range(m.shape[1]))):
    print("(%d,%d)   %5d        %5d" % (i, j, m[i, j], s[i, j]))
