"""74. Search a 2D Matrix
Solved
Medium
Topics
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 """class Solution(object):
    def searchMatrix(self, matrix, target):
        s=0
        k=len(matrix[0])
        e=k*len(matrix)-1
        while(s<=e):
            mid=(s+e)//2
            row=mid//k
            col=mid%k
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                s=mid+1
            else:
                e=mid-1
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        