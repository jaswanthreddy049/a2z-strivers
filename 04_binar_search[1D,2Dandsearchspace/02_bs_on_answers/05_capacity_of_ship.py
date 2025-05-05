"""1011. Capacity To Ship Packages Within D Days
Solved
Medium
Topics
Companies
Hint
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7"""
class Solution(object):
    def shipWithinDays(self, weights, days):
        def res(weights,days,mid):
            count=0
            ndays=1
            for i in weights:
                if count+i<=mid:
                    count+=i
                else:
                    ndays+=1
                    count=i
            return ndays<=days
        s=max(weights)
        e=sum(weights)
        while(s<=e):
            mid=(s+e)//2
            if res(weights,days,mid):
                result=mid
                e=mid-1
            else:
                s=mid+1
        return result


        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        