# Problem: Remove Nth Node From End of List
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use Two Pointers with a Dummy Node.
#
# Move the first pointer n steps ahead.
# Then move both pointers together until
# the first pointer reaches the end.
#
# The second pointer will be just before
# the node to be removed.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Starting from head instead of a dummy node.
# A dummy node handles edge cases such as
# removing the first node of the list.

# Revision Note:
# Gap Method:
# 1. Create dummy node.
# 2. Move first pointer n steps ahead.
# 3. Move both pointers together.
# 4. Delete dummy.next.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next