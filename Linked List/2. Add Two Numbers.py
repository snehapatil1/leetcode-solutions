"""
    Question:
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_string = ""
        num2_string = ""

        while l1:
            num1_string = num1_string + str(l1.val)
            l1 = l1.next
        
        while l2:
            num2_string = num2_string + str(l2.val)
            l2 = l2.next
        
        num1_string = ''.join(list(reversed(num1_string)))
        num1 = int(num1_string)
        num2_string = ''.join(list(reversed(num2_string)))
        num2 = int(num2_string)

        num3 = num1 + num2
        num3_op = list(reversed(str(num3)))

        output = ListNode(0)
        dummy = output
        
        for num in num3_op:
            node = ListNode(int(num))
            output.next = node
            output = node
        
        # print(dummy.next)
        return dummy.next
