"""242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 """
 class Solution(object):
    def isAnagram(self, s, t):
        mydict={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        for i in t:
            if i in mydict and mydict[i]>0:
                mydict[i]-=1
            else:
                return False
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        