class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = list1
        head2 = list2

        dummy = ListNode()
        ret = dummy

        while head1 and head2:

            if head1.val > head2.val:
                ret.next = head2
                head2 = head2.next

            else:
                ret.next = head1
                head1 = head1.next

            ret = ret.next

        while head1:
            ret.next = head1
            head1 = head1.next
            ret = ret.next

        while head2:
            ret.next = head2
            head2 = head2.next
            ret = ret.next

        return dummy.next