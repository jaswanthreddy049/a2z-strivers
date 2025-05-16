"""2. Add Two Numbers
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        dummy=ListNode(-1)
        temp=dummy
        c1=l1
        c2=l2
        while(c2 or carry or c1):
            val1=c1.val if c1 else 0
            val2=c2.val if c2 else 0
            s=val1+val2+carry
            carry=s//10
            temp.next=ListNode(s%10)
            temp=temp.next
            if c1:c1=c1.next 
            if c2:c2=c2.next
        return dummy.next         
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        