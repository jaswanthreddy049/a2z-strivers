"""1482. Minimum Number of Days to Make m Bouquets
Solved
Medium
Topics
Companies
Hint
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1."""
class Solution(object):
    def minDays(self, bloomDay, m, k):
        def res(bloomDay,m,k,day):
            flowers=0
            boq=0
            for i in bloomDay:
                if i<=day:
                    flowers+=1
                    if flowers==k:
                        boq+=1
                        flowers=0
                else:
                    flowers=0
            if boq>=m:return True
            else:return False
        s=min(bloomDay)
        e=max(bloomDay)
        if m*k>len(bloomDay):
            return -1
        while(s<=e):
            mid=(s+e)//2
            com=res(bloomDay,m,k,mid)
            if com:
                result=mid
                e=mid-1
            else:
                s=mid+1
        return result
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        