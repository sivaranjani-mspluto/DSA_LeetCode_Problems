class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #1. transpose --> 2. refection
        #transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #refection
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
        