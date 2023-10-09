# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        lList = []

        while head:
            lList.append(head.val)
            head = head.next
        
        return lList == lList[::-1]