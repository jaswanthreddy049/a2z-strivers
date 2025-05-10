"""234. Palindrome Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast=head
        slow=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        prev=None
        while(slow):
            nextnode=slow.next
            slow.next=prev
            prev=slow
            slow=nextnode
        temp=head
        while(prev):
            if prev.val!=temp.val:return False
            prev=prev.next
            temp=temp.next
        return True
        

        
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        