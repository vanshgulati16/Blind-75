
#Approach: The most efficient method to fid the middle node will be to have two pointers one will be fast pointer which will jump 2 nodes from the source position 
# and another be slow which will jump 1 postion from the source and will have a prev node to keep the visited node, once th fast node reach the NULL we will set
# prev next pointer to slow pointer's next pointing address. which will hence delete the middle node which is slow node.
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None
        
        if head is None or head.next is None:
            return
        while fast is not None and fast.next is not None:
            fast= fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

        return head 
