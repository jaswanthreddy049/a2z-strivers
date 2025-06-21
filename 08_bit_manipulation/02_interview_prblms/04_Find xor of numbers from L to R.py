"""Given two integers L and R. Find the XOR of the elements in the range [L , R].


Examples:
Input : L = 3 , R = 5

Output : 2

Explanation : answer = (3 ^ 4 ^ 5) = 2."""
class Solution:      
    def findRangeXOR(self, l, r):
        def res(n):
            if n%4==1:
                return 1
            if n%4==2:
                return n+1
            if n%4==3:
                return 0
            if n%4==0:
                return n
        return res(l-1)^res(r)
            
        #your code goes here