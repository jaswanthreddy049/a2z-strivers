"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""
class Solution(object):
    def isPalindrome(self, s):
        mylist=[]
        for i in s:
            if i.isalpha() or i.isalnum():
                mylist.append(i.lower())
        def mypalindrome(start,end):
            if start>=end:
                return True
            if mylist[start]!=mylist[end]:
                return False
            return mypalindrome(start+1,end-1)
        return mypalindrome(0,len(mylist)-1)



        
        
        """
        :type s: str
        :rtype: bool
        """
        