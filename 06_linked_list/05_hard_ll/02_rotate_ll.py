"""61. Rotate List
Solved
Medium
Topics
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        cur=head
        count=0
        while(cur):
            cur=cur.next
            count+=1
        s=k%count
        while(s>0):
            cur=head
            while(cur and cur.next):
                prev=cur
                cur=cur.next
            prev.next=None
            cur.next=head
            head=cur
            s-=1
        return head

            

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        