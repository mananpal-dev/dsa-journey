# Problem: Merge Two Sorted Lists
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use a dummy node to simplify merging.
#
# Compare the current nodes of both lists.
# Attach the smaller node to the merged list.
# Move the corresponding pointer forward.
#
# After one list is exhausted,
# attach the remaining nodes of the other list.

# Time Complexity: O(n + m)
# n = length of list1
# m = length of list2

# Space Complexity: O(1)

# Common Mistake:
# Writing:
# while list1 and list1:
#
# Correct:
# while list1 and list2:
#
# Both lists must have remaining nodes before comparing them.

# Revision Note:
# Dummy Node Pattern:
# 1. Create dummy node.
# 2. Use current pointer to build the answer.
# 3. Return dummy.next.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy

        while list1 and list2:

            if list1.val > list2.val:

                cur.next = list2
                list2 = list2.next

            else:

                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next