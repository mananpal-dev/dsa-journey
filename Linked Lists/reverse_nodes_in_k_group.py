# Problem: Reverse Nodes in k-Group
# Platform: LeetCode
# Difficulty: Hard

# Approach:
# Use Recursion.
#
# 1. Check if there are at least k nodes.
# 2. Reverse the first k nodes.
# 3. Recursively reverse the remaining list.
# 4. Connect the reversed group with the result
#    of the recursive call.

# Time Complexity: O(n)
# Space Complexity: O(n / k)
# (Recursion stack)

# Common Mistake:
# Reversing the last group even when it
# contains fewer than k nodes.
# Always check if k nodes exist before reversing.

# Revision Note:
# Pattern:
# Count k nodes
# ↓
# Reverse current group
# ↓
# Recursively process remaining nodes
# ↓
# Connect both parts

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        if not head:
            return None

        tail = head

        # Check if at least k nodes exist
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next

        # Reverse nodes from head to tail (exclusive)
        def reverse(cur, end):
            prev = None

            while cur != end:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            return prev

        new_head = reverse(head, tail)

        # Connect current group with remaining groups
        head.next = self.reverseKGroup(tail, k)

        return new_head