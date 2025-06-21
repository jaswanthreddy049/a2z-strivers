"""231. Power of Two
Solved
Easy
Topics
premium lock icon
Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

"""
class Solution(object):
    def isPowerOfTwo(self, n):
        count=0
        if n<0:return False
        while(True):
            if n==(1<<count):
                return True
            if n<(1<<count):
                return False
            count+=1

        """
        :type n: int
        :rtype: bool
        """
        