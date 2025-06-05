"""424. Longest Repeating Character Replacement
Solved
Medium
Topics
premium lock icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too."""
class Solution(object):
    def characterReplacement(self, s, k):
        l,r=0,0
        res=0
        maxi=0
        freq=defaultdict(int)
        while(r<len(s)):
            freq[s[r]]+=1
            maxi=max(maxi,freq[s[r]])
            if (r-l+1)-maxi>k:
                freq[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        