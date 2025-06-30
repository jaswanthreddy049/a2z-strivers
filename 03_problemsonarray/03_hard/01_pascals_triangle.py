"""118. Pascal's Triangle
Solved
Easy
Topics
premium lock icon
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]"""
class Solution(object):
    def generate(self, numRows):
        result=[]
        prev=[1]
        new=[]
        result.append(prev)
        for i in range(1,numRows):
            new.append(1)
            for j in range(len(prev)-1):
                new.append(prev[j]+prev[j+1])
            new.append(1)
            prev=[]
            prev=new
            result.append(new)
            new=[]
        return result


        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        