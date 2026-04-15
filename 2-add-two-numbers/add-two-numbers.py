# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy

        carry=0
        # if 7+8=15 (carry 1 must be there)
        while l1 or l2 or carry: 
            d1=l1.val if l1 else 0
            d2=l2.val if l2 else 0
            tot = d1+d2+carry
            carry=tot//10
            tot=tot%10
            curr.next=ListNode(tot)

            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next


