"""Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6."""

class Solution:
    def longestSubarray(self, arr, k):  
        my={}
        maxlen=0
        prefix=0
        for i in range(len(arr)):
            prefix+=arr[i]
            if prefix==k:
                maxlen=max(maxlen,i+1)
            if prefix-k in my:
                maxlen=max(maxlen,i-my[prefix-k])
            if prefix not in my:
                my[prefix]=i
        return maxlen
        # code here