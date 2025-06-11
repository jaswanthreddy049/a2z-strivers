"""2104. Sum of Subarray Ranges
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59."""
class Solution(object):
    def subArrayRanges(self, nums):
        n = len(nums)
        mod = 10**9 + 7

        def sum_of_mins():
            prev_smaller = [-1] * n
            next_smaller = [n] * n
            stack = []
            for i in range(n):
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                if stack:
                    prev_smaller[i] = stack[-1]
                stack.append(i)

            stack = []
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    next_smaller[i] = stack[-1]
                stack.append(i)

            total = 0
            for i in range(n):
                left = i - prev_smaller[i]
                right = next_smaller[i] - i
                total += nums[i] * left * right
            return total

        def sum_of_maxs():
            prev_greater = [-1] * n
            next_greater = [n] * n
            stack = []
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                if stack:
                    prev_greater[i] = stack[-1]
                stack.append(i)

            stack = []
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                if stack:
                    next_greater[i] = stack[-1]
                stack.append(i)

            total = 0
            for i in range(n):
                left = i - prev_greater[i]
                right = next_greater[i] - i
                total += nums[i] * left * right
            return total

        return sum_of_maxs() - sum_of_mins()
