"""
Code
Testcase
Testcase
Test Result
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 """
 class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]
        s=len(first)-1
        r=len(last)-1
        res=""
        i=0
        while(i<=s and i<=r):
            if first[i]==last[i]:
                res+=first[i]
                i+=1
            else:break
        return res