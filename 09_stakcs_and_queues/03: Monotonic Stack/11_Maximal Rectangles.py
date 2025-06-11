"""85. Maximal Rectangle
Solved
Hard
Topics
premium lock icon
Companies
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        def lhisto(heights):
            stack=[]
            n=len(heights)
            nsl=[n]*n
            psl=[-1]*n
            for i in range(n):
                while(stack and heights[stack[-1]]>heights[i]):
                    stack.pop()
                if stack :
                    psl[i]=stack[-1]
                stack.append(i)
            stack=[]
            for i in range(n-1,-1,-1):
                while(stack and heights[stack[-1]]>=heights[i]):
                    stack.pop()
                if stack :
                    nsl[i]=stack[-1]
                stack.append(i)
            result=0
            for i in range(n):
                result=max(result,heights[i]*(nsl[i]-psl[i]-1))
            return result
        n=len(matrix)
        m=len(matrix[0])
        ps = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m):
            sum=0
            for i in range(n):
                if matrix[i][j]=="0":
                    sum=0
                else:
                    sum+=1
                ps[i][j]=sum
        result=0
        for i in range(n):
            result=max(result,lhisto(ps[i]))
        return result
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        