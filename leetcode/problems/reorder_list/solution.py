# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow will reach mid when fast will reach end of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow's next node will be list2 start
        list2 = slow.next
        slow.next = None
        prev = None
        
        # reverse list2
        while list2:
            nxt = list2.next
            list2.next = prev
            prev = list2
            list2 = nxt
        
        # list1 will be original head and list2 will be reversed list
        list1, list2 = head, prev

        # merge list1 and list2
        while list2:
            l1nxt, l2nxt = list1.next, list2.next
            list1.next = list2
            list2.next = l1nxt
            list1 = l1nxt
            list2 = l2nxt
        

