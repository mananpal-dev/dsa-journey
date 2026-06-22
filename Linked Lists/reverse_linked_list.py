# Problem: Reverse Linked List
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Reverse the linked list iteratively using three pointers.
#
# node -> Previous node.
# head -> Current node.
# temp -> Stores the next node before changing links.
#
# At each step:
# 1. Save the next node.
# 2. Reverse the current node's pointer.
# 3. Move both pointers one step ahead.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting to save head.next before reversing.
# Once head.next is changed, the remaining list is lost.

# Revision Note:
# Three Pointer Technique:
# prev (node)
# curr (head)
# next (temp)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = None

        while head:

            temp = head.next
            head.next = node

            node = head
            head = temp

        return node