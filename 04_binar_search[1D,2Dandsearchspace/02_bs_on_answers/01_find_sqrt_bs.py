class Solution:
    def floorSqrt(self, n: int) -> int:
        start=0
        end=n
        while(start<=end):
            mid=(start+end)//2
            if mid*mid<=n:
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans
