import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    n = len(A)
    m = len(A[0])
    B = np.transpose(A)*0
    for i in range(0,m,1):
        for j in range(0,n,1):
            B[i][j] = A[j][i]
            
    return B
    pass
