
"""Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Input: arr[] = [1, 3 , 2]
Output: [1, 2, 3]
"""
class Solution:
    def merge(self,arr,l,mid,r):
        myarr=[]
        left=l
        right=mid+1
        while(left<=mid and right<=r):
            if arr[left]<=arr[right]:
                myarr.append(arr[left])
                left+=1
            else:
                myarr.append(arr[right])
                right+=1
        while(left<=mid):
                myarr.append(arr[left])
                left+=1
        while(right<=r):
                myarr.append(arr[right])
                right+=1
        for i in range(len(myarr)):
            arr[l+i]=myarr[i]
        
        
 
    def mergeSort(self,arr,l,r):
        if l==r:
            return
        mid=(l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)