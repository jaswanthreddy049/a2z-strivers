"""76. Minimum Window Substring
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window."""
class Solution(object):
    def minWindow(self, s, t):
        freq=defaultdict(int)
        for i in t:
            freq[i]+=1
        index=-1
        minlen=float('inf')
        l,r=0,0
        count=0
        while(r<len(s)):
            if freq[s[r]]>0:
                count+=1
            freq[s[r]]-=1
            while(count==len(t)):
                if r-l+1<minlen:
                    minlen=r-l+1
                    index=l
                freq[s[l]]+=1
                if freq[s[l]]>0:
                    count-=1
                l+=1

            r+=1
        if index==-1:return ""
        else: return s[index:index+minlen]


        """
        :type s: str
        :type t: str
        :rtype: str
        """
        