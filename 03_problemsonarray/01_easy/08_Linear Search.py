"""Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

Examples:

Input: arr[] = [1, 2, 3, 4, 6], k = 6
Output: true
Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
Input: arr[] = [1, 2, 4, 5, 6], k = 3
Output: false
Exlpanation: Since, 3 is not present in the array, output is false."""
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        for i in range(len(arr)):
            if arr[i]==k:
                return True
        return False