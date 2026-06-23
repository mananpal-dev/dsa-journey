# Problem: Linked List Cycle
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use Floyd's Cycle Detection Algorithm (Tortoise and Hare).
#
# slow -> moves one step at a time.
# fast -> moves two steps at a time.
#
# If a cycle exists, both pointers will eventually meet.
# If fast reaches the end of the list,
# then no cycle exists.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Using:
# while fast:
#
# Since fast moves two steps (fast.next.next),
# you must also ensure fast.next exists.

# Revision Note:
# Slow Pointer = 1 step
# Fast Pointer = 2 steps
#
# If they meet -> Cycle exists.
# If fast reaches None -> No cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False