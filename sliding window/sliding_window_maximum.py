# Problem: Sliding Window Maximum
# Platform: LeetCode
# Difficulty: Hard

# Approach:
# Use a monotonic decreasing deque.
# Remove smaller elements from the back because
# they can never become the maximum while a larger
# element exists to their right.
# The front of the deque always stores the maximum.

# Time Complexity: O(n)
# Space Complexity: O(k)

# Common Mistake:
# Forgetting to remove the outgoing element when
# it leaves the sliding window.

# Revision Note:
# Classic Monotonic Queue problem.
# Important for advanced Sliding Window questions.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        q = deque()

        for idx, num in enumerate(nums):

            while q and q[-1] < num:
                q.pop()

            q.append(num)

            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()

            if idx >= k - 1:
                res.append(q[0])

        return res