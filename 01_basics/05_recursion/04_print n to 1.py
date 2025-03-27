"""
Print numbers from N to 1 (space separated) without the help of loops.
Input:
N = 10
Output: 10 9 8 7 6 5 4 3 2 1
Your Task:
This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.
"""
class Solution:
    def printNos(self, n):
        if n<1:
            return
        print(n,end=" ")
        self.printNos(n-1)