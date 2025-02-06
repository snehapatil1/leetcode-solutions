# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[-1]
        
        for i in range(1, len(lists)):
            lt3 = self.mergeTwoLists(lists[i], lists[i - 1])
            lists[i] = lt3
        
        return lists[-1]
    
    def mergeTwoLists(self, lt1, lt2):
        merged = ListNode()
        dummy = merged
        while lt1 and lt2:
            if lt1.val <= lt2.val:
                merged.next = lt1
                lt1 = lt1.next
            else:
                merged.next = lt2
                lt2 = lt2.next
            merged = merged.next
        if lt1:
            merged.next = lt1
            merged = merged.next
            lt1 = lt1.next
        if lt2:
            merged.next = lt2
            merged = merged.next
            lt2 = lt2.next
        return dummy.next
            
