"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
class Solution(object):
    def reverse(self, x):
        reverse=0
        temp=x
        if x<0:
            x=-(x)
        while(x>0):
            rem=x%10
            reverse=reverse*10+rem
            x=x//10
        if reverse<= -(2**31) or reverse>=(2**31)-1:
            return 0
        elif temp<0:
            return -reverse
        else:
            return reverse