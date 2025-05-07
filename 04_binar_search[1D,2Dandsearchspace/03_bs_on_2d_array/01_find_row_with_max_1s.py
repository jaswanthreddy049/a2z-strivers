"""Find row with maximum 1's
100
Easy
Hint
Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.

If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1.


Examples:
Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]

Output: 0

Explanation: The row with the maximum number of ones is 0 (0 - indexed).

Input: mat = [ [0, 0], [0, 0] ]

Output: -1

Explanation: The matrix does not contain any 1. So, -1 is the answer."""
class Solution:
    def rowWithMax1s(self, mat):
        maxco=0
        index=-1
        for i in range(len(mat)-1):
            s=0
            e=len(mat[0])-1
            while(s<=e):
                mid=(s+e)//2
                if mat[i][mid]>0:
                    e=mid-1
                else:
                    s=mid+1
            ans=len(mat[0])-s
            if maxco<ans:
                maxco=ans
                index=i
        return index

       