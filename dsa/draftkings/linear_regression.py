import numpy as np

"""
performs linear regression using the normal equation: β=(𝑋^𝑇 * 𝑋)^−1 * 𝑋^𝑇 * y, where
    X is the matrix of input features
    y is the vector of output values
    β is the vector of coefficients

Time Complexity: 𝑂(𝑛^3)
1. Extract Features and Targets:
   list comprehensions iterate over each row of `a`, where `a` is an 𝑛 × (𝑑 + 1) matrix (with 𝑛 rows and 𝑑 + 1 columns)
   both operations take 𝑂(𝑛𝑑), because for each row (total 𝑛), it processes 𝑑 elements for 𝑋 and 1 element for 𝑦
2. Transpose Matrix 𝑋 -> transposing a matrix of size 𝑛 × 𝑑 involves rearranging its elements
   𝑂(𝑛𝑑), as it needs to access and reposition each element once.
3. Compute Coefficients -> 𝑂(𝑛𝑑)
   Matrix Multiplication 𝑋 subscript 𝑇 @ 𝑋 -> multiplies 𝑋^𝑇 of size 𝑑 × 𝑛 by 𝑋 of size 𝑛 × 𝑑 -> 𝑂(𝑛𝑑^2)
   Matrix Inversion inv(𝑋 subscript 𝑇 @ 𝑋) -> inverts a 𝑑 × 𝑑 matrix -> 𝑂(𝑑^3) using Gaussian elimination or similar
   Matrix Multiplication inv(𝑋 subscript 𝑇 @ 𝑋) @ 𝑋 subscript 𝑇 -> 
     multiplies the inverse 𝑑 × 𝑑 matrix with 𝑋^𝑇 of size 𝑑 × 𝑛 -> 𝑂(𝑛𝑑^2)
   Matrix Multiplication (inv(𝑋 subscript 𝑇 @ 𝑋) @ 𝑋 subscript 𝑇) @ 𝑦 -> 
     multiplies the resulting 𝑑 × 𝑛 with 𝑦 of size 𝑛 -> 𝑂(𝑛𝑑)
4. Return Results -> converts matrices to lists -> 𝑂(𝑛𝑑 + 𝑑^2), 
   where 𝑛𝑑 for converting 𝑋 subscript 𝑇 and 𝑑 for coefficients
Combining all steps, the total time complexity is -> 𝑂(𝑛𝑑^2 + 𝑑^3)

Space Complexity: 𝑂(𝑛𝑑)
1. Extract Features and Targets -> 𝑂(𝑛𝑑) for 𝑋 and 𝑂(𝑛) for 𝑦
   stores 𝑋 as an 𝑛 × 𝑑 matrix and 𝑦 as an 𝑛-element vector
2. Transpose Matrix 𝑋 -> 𝑂(1), assuming that NumPy transpose operation is a view
   transposing a matrix does not create a new copy but gives a new view on original data
3. Compute Coefficients
   Matrix Multiplication 𝑋 subscript 𝑇 @ 𝑋 creates a 𝑑 × 𝑑 matrix -> 𝑂(𝑑^2)
   Matrix Inversion inv(𝑋 subscript 𝑇 @ 𝑋) stores the inverse matrix of size 𝑑 × 𝑑 -> 𝑂(𝑑^2)
   Matrix Multiplication (inv(𝑋 subscript 𝑇 @ 𝑋) @ 𝑋 subscript 𝑇) @ 𝑦 
     intermediate results of size 𝑑 × 𝑛 and 𝑑 × 1 -> 𝑂(𝑛𝑑)
4. Return Results -> 𝑂(𝑛𝑑) for 𝑋 subscript 𝑇 and 𝑂(𝑑) for coefficients
   Converts matrices to lists
"""


def linear_regression(a):
    X = np.array([row[:-1] for row in a])
    y = np.array([row[-1] for row in a])
    X_T = X.T
    coefficients = np.linalg.inv(X_T @ X) @ X_T @ y

    return [X_T.tolist(), coefficients.tolist()]


A = [[1, 5], [4, 8], [5, 9]]
print(linear_regression(A))
# Output: [[[1, 4, 5], [5, 8, 9]], [4.1, 0.9]]
