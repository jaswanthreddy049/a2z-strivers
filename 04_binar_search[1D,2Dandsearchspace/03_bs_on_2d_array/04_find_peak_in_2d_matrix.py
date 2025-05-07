"""1901. Find a Peak Element II
Solved
Medium
Topics
Companies
Hint
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
"""class Solution(object):
    def findPeakGrid(self, mat):
        def res(mat,col,n):
            maxco=-1
            index=-1
            for i in range(n):
                if mat[i][col]>maxco:
                    maxco=mat[i][col]
                    index=i
            return index
        s=0
        e=len(mat[0])-1
        while(s<=e):
            mid=(s+e)//2
            ans=res(mat,mid,len(mat))
            if mid-1>=0:
                left=mat[ans][mid-1]
            else:
                left=-1
            if mid+1>=len(mat[0]):
                right=-1
            else:
                right=mat[ans][mid+1]
            if left<mat[ans][mid] and mat[ans][mid]>right:
                return [ans,mid]
            elif left>mat[ans][mid]:e=mid-1
            else:s=mid+1
        return [-1,-1]


        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        