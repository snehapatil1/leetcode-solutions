# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        linkedListLen = 0
        output = []
        curr = head
        while curr:
            linkedListLen += 1
            curr = curr.next
        
        size, remainder = divmod(linkedListLen, k)

        temp = head
        for i in range(k):
            output.append(temp)
            current_part_size = size + 1 if remainder > 0 else size
            remainder -= 1
            for j in range(current_part_size - 1):
                temp = temp.next
            if temp:
                temp.next, temp = None, temp.next

        return output
        