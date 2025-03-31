"""Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order. Given an array, arr[], with starting index low and ending index high, complete the functions partition() and quickSort(). Use the last element as the pivot so that all elements less than or equal to the pivot come before it, and elements greater than the pivot follow it.

Note: The low and high are inclusive.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: After sorting, all elements are arranged in ascending order.
Input: arr[] = [2, 1, 6, 10, 4, 1, 3, 9, 7]
Output: [1, 1, 2, 3, 4, 6, 7, 9, 10]
Explanation: Duplicate elements (1) are retained in sorted order.
"""
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low>high:
            return
        part=self.partition(arr,low,high)
        self.quickSort(arr,low,part-1)
        self.quickSort(arr,part+1,high)
    def partition(self,arr,low,high):
        pivot=low
        i=low
        j=high
        while(i<j):
            while(i<=high-1 and arr[i]<=arr[pivot]):
                i+=1
            while(j>=low+1 and arr[j]>=arr[pivot]):
                j-=1
            if i<j:
                arr[j],arr[i]=arr[i],arr[j]
        arr[pivot],arr[j]=arr[j],arr[pivot]
        return j