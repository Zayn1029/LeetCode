# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while True:
            # 檢查剩餘節點是否大於等於k
            temp = pre
            for _ in range(k):
                temp = temp.next
                if not temp:
                    return dummy.next
            
            # 進行k個節點的反轉
            curr = pre.next
            nxt = curr.next
            
            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = curr.next
            
            pre = curr