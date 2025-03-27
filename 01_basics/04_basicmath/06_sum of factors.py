"""Given a positive integer n, The task is to find the value of Σi F(i) where i is from 1 to n and function F(i) is defined as the sum of all divisors of i.

Examples:

Input: n = 4
Output: 15
Explanation:
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
So, F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7 = 15
    """
class Solution:
    def sumOfDivisors(self, n):
        count=0
        for i in range(1,n+1):
            s=i
            j=1
            while(j*j<=s):
                if s%j==0:
                    count+=j
                    if j!=s//j:
                        count+=s//j
                j+=1
        return count
