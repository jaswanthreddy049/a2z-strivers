"""Given two integers a and b, the task is to compute their LCM and GCD and return an array containing their LCM and GCD.

Examples:

Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
Input: a = 14 , b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.
Input: a = 1 , b = 1
Output: [1, 1]
Explanation: LCM of 1 and 1 is 1, while their GCD is 1.
"""
class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        temp1=a
        temp2=b
        if b>a:
            a=a+b
            b=a-b
            a=a-b
        rem=1
        while(rem!=0):
            rem=a%b
            a=b
            b=rem
        lcm=(temp1*temp2)//a
        return [lcm,a]