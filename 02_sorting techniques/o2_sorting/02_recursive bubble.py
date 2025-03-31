""""""
Given an array, arr[]. Sort the array using bubble sort algorithm.

Examples :

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
""""""
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        def mybubble(i):
            if i>len(arr)-1:
                return
            for j in range(0,len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            mybubble(i+1)
        mybubble(0)