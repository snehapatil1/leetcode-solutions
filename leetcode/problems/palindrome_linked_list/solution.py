# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_list = []
        current = head
        while current:
            reversed_list.append(current.val)
            current = current.next
        return reversed_list == reversed_list[::-1]
                
                