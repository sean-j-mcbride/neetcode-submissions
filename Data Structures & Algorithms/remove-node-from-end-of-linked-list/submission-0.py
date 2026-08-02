# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N = 0

        while curr:
            N += 1
            curr = curr.next
        
        idx = N - n
        if idx == 0:
            return head.next

        curr = head
        N = 0

        while curr:
            if (N + 1) == idx:
                curr.next = curr.next.next
                break
            curr = curr.next
            N += 1
        return head