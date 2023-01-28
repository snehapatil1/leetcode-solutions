# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, node = 0, head

        # get count of elements in linked list
        while node:
            node = node.next
            count += 1
        
        # if length of linked list is same as n then return next
        if count == n:
            return head.next
        
        # set node = linked list same as head provided
        node = ListNode(0, head)
        
        # iterate the node linked list until last nth element
        for i in range(0, count - n):
            node = node.next

        # if node is present on nth position then set next to nth next node
        if node:
            node.next = node.next.next
        
        return head