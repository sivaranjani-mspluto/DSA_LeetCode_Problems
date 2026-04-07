# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast= head,head
        #make the slow as mid and fast to end
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #split into two
        temp=slow.next
        slow.next=None

        #reverse the second list
        prev=None
        while temp:
            Next=temp.next
            temp.next=prev
            prev=temp
            temp=Next

        #merge the two
        head1=head
        head2=prev
        while head1 !=None and head2 !=None:
            head1next=head1.next
            head2next=head2.next

            head1.next=head2
            head1=head1next
            head2.next=head1
            head2=head2next
        return 


        