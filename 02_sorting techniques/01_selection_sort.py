"""
Given an array arr, use selection sort to sort arr[] in increasing order.

Examples :

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: Maintain sorted (in bold) and unsorted subarrays. Select 1. Array becomes 1 4 3 9 7. Select 3. Array becomes 1 3 4 9 7. Select 4. Array becomes 1 3 4 9 7. Select 7. Array becomes 1 3 4 7 9. Select 9. Array becomes 1 3 4 7 9.
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)-1):
            mini=i
            for j in range(i+1,len(arr)):
                if arr[mini]>arr[j]:
                    mini=j
            if i!=mini:
                arr[i],arr[mini]=arr[mini],arr[i]
        return arr