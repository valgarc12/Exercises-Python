"""
You are given an m x n matrix. Your task is to determine if the matrix has diagonal stripes where all elements in each diagonal from top-left to bottom-right are of the same stripe—that is, they are identical.

In this context, each diagonal stripe runs from the top-left corner to the bottom-right corner of the matrix. Check if every diagonal stripe consists entirely of the same number.

Return True if all diagonal stripes are of the same stripe, otherwise return False."""


matrix = [
    [1, 2, 3],
    [4, 1, 2],
    [7, 4, 1]
]

def samestripes(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j] != matrix[i +1][j+1]:
                return False
    return True

print(samestripes(matrix))        
        