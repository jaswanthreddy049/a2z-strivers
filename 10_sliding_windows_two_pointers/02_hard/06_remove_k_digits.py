"""402. Remove K Digits
Solved
Medium
Topics
premium lock icon
Companies
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes."""
class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        if len(num)==k:
            return "0"
        for i in num:
            while(stack and k>0 and stack[-1]>i):
                stack.pop()
                k-=1
            stack.append(i)
        while(k>0):
            stack.pop()
            k-=1
        if not stack:
             return "0"
        stack.reverse()
        while(stack and stack[-1]=="0"):
            stack.pop()
        stack.reverse()
        result="".join(stack)

        return result if result else "0"


        """
        :type num: str
        :type k: int
        :rtype: str
        """
        