"""Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7."""
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        union=[]
        i=0
        j=0
        while(i<len(a) and j<len(b)):
            if a[i]<b[j]:
                if len(union)==0 or union[-1]<a[i]:
                    union.append(a[i])
                i+=1
            elif a[i]>b[j]:
                if len(union)==0 or union[-1]<b[j]:
                    union.append(b[j])
                j+=1
            else:
                if len(union)==0 or union[-1]<a[i]:
                    union.append(a[i])
                j+=1
                i+=1
        while(i<len(a)):
            if len(union)==0 or union[-1]<a[i]:
                union.append(a[i])
            i+=1
        while(j<len(b)):
            if len(union)==0 or union[-1]<b[j]:
                union.append(b[j])
            j+=1
        return union