# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create linked list to do merging operation
        mergedList = ListNode()
        # create another linked list to maintain copy of merged linked list
        newList = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                # if list1 val is smaller than list2 val then set that in merged list and iterate to next element of list1
                mergedList.next = list1
                list1 = list1.next
            else:
                # if list2 val is smaller than list1 val then set that in merged list and iterate to next element of list2
                mergedList.next = list2
                list2 = list2.next
            
            # move pointer to next node of merged list
            mergedList = mergedList.next

        # if there are nodes left in list1 then add all as it is to the merged list
        if list1:
            mergedList.next = list1
        
        # if there are nodes left in list2 then add all as it is to the merged list
        if list2:
            mergedList.next = list2
        
        # return another copy of list which is pointing to merged list head
        return newList.next


