class Solution:
     def pairSum(self, head: Optional[ListNode]) -> int:
        # step 1: find middle
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev = None
        curr = slow.next

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # step 3: two pointer sum
        left = head
        right = prev  # head of reversed second half
        max_sum = 0

        while right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next

        return max_sum