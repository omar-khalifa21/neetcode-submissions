
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        combined_node = ListNode()
        head = combined_node

        while list1 is not None and list2 is not None:
            val_1 = list1.val 
            val_2 = list2.val
            if val_1 < val_2:
                combined_node.next = list1
                list1 = list1.next
            else:
                combined_node.next = list2
                list2 = list2.next
            combined_node = combined_node.next
        
        if list1 is not None or list2 is not None:
            remaining = list1 if list1 else list2
            while remaining is not None:
                combined_node.next = remaining
                remaining = remaining.next
                combined_node = combined_node.next
        
        return head.next