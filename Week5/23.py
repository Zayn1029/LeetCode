class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        return self.merge_lists(lists, 0, len(lists) - 1)
    
    def merge_lists(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        l1 = self.merge_lists(lists, left, mid)
        l2 = self.merge_lists(lists, mid + 1, right)
        
        return self.merge_two_lists(l1, l2)
    
    def merge_two_lists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2
        return dummy.next