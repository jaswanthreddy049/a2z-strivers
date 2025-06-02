"""1358. Number of Substrings Containing All Three Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1"""
class Solution(object):
    def numberOfSubstrings(self, s):
        l,r=0,0
        result=0
        freq={"a":0,"b":0,"c":0}
        while(r<len(s)):
            freq[s[r]]+=1
            while(freq[a]>0 and freq[b]>0 and freq[c]>0):
                result+=len(s)-r
                freq[s[l]]-=1
                l+=1
            r+=1
        return result
        """
        :type s: str
        :rtype: int
        """
        