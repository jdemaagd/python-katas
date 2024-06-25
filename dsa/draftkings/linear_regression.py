import numpy as np


def linear_regression(a):
    X = np.array([row[:-1] for row in a])
    y = np.array([row[-1] for row in a])
    X_T = X.T
    coefficients = np.linalg.inv(X_T @ X) @ X_T @ y
    return [X_T.tolist(), coefficients.tolist()]


A = [[1, 5], [4, 8], [5, 9]]
print(linear_regression(A))
# Output: [[[1, 4, 5], [5, 8, 9]], [4.1, 0.9]]
