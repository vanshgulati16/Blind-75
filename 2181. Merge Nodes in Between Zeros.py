# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head.next
        ans = 0
        while curr is not None:
            if curr.val !=0:
                ans += curr.val
            else:
                prev.val = ans
                prev.next = curr.next
                prev = prev.next
                ans = 0
            curr = curr.next
        return head.next
