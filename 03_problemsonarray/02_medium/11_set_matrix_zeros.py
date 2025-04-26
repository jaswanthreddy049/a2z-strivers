"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]"""
class Solution(object):
    def setZeroes(self, matrix):
        row=[0]*len(matrix)
        col=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]==1:
                    matrix[i][j]=0
        return matrix
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        