"""Print GFG n times without the loop.
Example:
Input:
5
Output:
GFG GFG GFG GFG GFG
Your Task:
This is a function problem. You only need to complete the function printGfg() that takes N as parameter and prints N times GFG recursively. Don't print newline, it will be added by the driver code.
""""
class Solution:    
    #Complete this function
    def printNos(self,n):
        if n<1:
            return
        self.printNos(n-1)
        print(n ,end=" ")