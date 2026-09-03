# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        end = head
        while end:
            length += 1
            end = end.next

        temp = ListNode(0, head)
        prev = temp

        for _ in range(length - n):
            prev = prev.next
        prev.next = prev.next.next

        return temp.next
        
