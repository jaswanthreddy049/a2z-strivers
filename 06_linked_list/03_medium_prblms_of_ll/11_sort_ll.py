"""148. Sort List
Solved
Medium
Topics
Companies
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        cur=head
        arr=[]
        while(cur):
            arr.append(cur.val)
            cur=cur.next
        arr.sort()
        cur=head
        i=0
        while(cur):
            cur.val=arr[i]
            i+=1
            cur=cur.next
        return head

                    
                    
            
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        