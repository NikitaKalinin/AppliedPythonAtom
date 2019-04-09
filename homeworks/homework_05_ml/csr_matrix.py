#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix
    """
    def __init__(self, init_matrix_representation):
        """
        :param init_matrix_representation: can be usual dense matrix
        or
        (row_ind, col, data) tuple with np.arrays,
        where data, row_ind and col_ind satisfy the relationship:
        a[row_ind[k], col_ind[k]] = data[k]
        """
        init = init_matrix_representation
        if isinstance(init_matrix_representation, tuple) and len(init_matrix_representation) == 3:
            init = list(init)
            matrix = np.zeros((max(init[0]) + 1, max(init[1]) + 1))
            for i in range(len(init[2])):
                matrix[init[0][i], init[1][i]] = init[2][i]
            to_csr = CSRMatrix(matrix)
            self.ia = to_csr.ia
            self.a = to_csr.a
            self.ja = to_csr.ja
            self.columns = matrix.shape[1]
        elif isinstance(init_matrix_representation, np.ndarray):
            self.a = init[init != 0]
            self.ja = np.nonzero(init)[1]
            self.columns = init.shape[1]
            self.ia = np.array([0]*(init.shape[0]+1))
            for i in range(1, len(self.ia)):
                self.ia[i] = self.ia[i-1] + np.count_nonzero(init[i-1])
        else:
            raise ValueError

    def get_item(self, i, j):
        """
        Return value in i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if (len(self.ia) - 1) >= i >= 0 and self.columns >= j >= 0:
            c = self.ia[i]
            while c < self.ia[i+1]:
                if self.ja[c] == j:
                    return self.a[c]
                c += 1
            return 0

    def set_item(self, i, j, value):
        """
        Set the value to i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        matrix = self.to_dense()
        matrix[i, j] = value
        new_m = CSRMatrix(matrix)
        self.ia = new_m.ia
        self.a = new_m.a
        self.ja = new_m.ja

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        out = np.zeros((len(self.ia)-1, self.columns))
        for row in range(len(self.ia) - 1):
            for col in range(self.columns):
                out[row, col] = self.get_item(row, col)
        return out
