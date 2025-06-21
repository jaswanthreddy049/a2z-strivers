"""29. Divide Two Integers
Solved
Medium
Topics
premium lock icon
Companies
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231."""
class Solution(object):
    def divide(self, dividend, divisor):
        status=True
        if dividend>0 and divisor<0:status=False
        if divisor>0 and dividend<0:status=False
        dividend=abs(dividend)
        divisor=abs(divisor)
        ans=0
        while(dividend>=divisor):
            count=0
            while(dividend>=divisor<<(count+1)):
                count+=1
            ans+=1<<count
            dividend=dividend-(divisor<<count)
        if ans>2**31-1 and status:
            return 2**31-1
        if not status:ans=-ans
        if ans<(-2**31):
            return -2**31
        return ans

        
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        