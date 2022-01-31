class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
        return head
