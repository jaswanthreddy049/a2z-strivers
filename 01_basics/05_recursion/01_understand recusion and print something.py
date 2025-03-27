"""Print 1 To N Without Loop
Difficulty: BasicAccuracy: 61.33%Submissions: 301K+Points: 1
Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes n as a parameter and prints the number from 1 to n recursively.

Note: Don't print any newline, it will be added by the driver code.

Examples:

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Input: n = 5
Output: 1 2 3 4 5"""
class Solution:    
    #Complete this function
    def printNos(self,n):
        if n<1:
            return
        self.printNos(n-1)
        print(n ,end=" ")