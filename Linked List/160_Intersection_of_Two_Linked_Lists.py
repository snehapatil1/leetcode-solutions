# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if (not headA) or (not headB):
            return None
        
        visites_headA_nodes = set()
        
        while headA:
            visites_headA_nodes.add(headA)
            headA = headA.next
        
        while headB:
            if headB in visites_headA_nodes:
                return headB
            headB = headB.next
        
        return None
