"""Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5."""
class Solution:
    def largest(self, arr):
        large=0
        for i in arr:
            if i>large:
                large=i
        return large