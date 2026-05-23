# Problem: Top K Frequent Elements
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Count frequency using hashmap.
# Store elements according to frequency using bucket sort.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting that frequency can go up to len(nums),
# so bucket array size should be len(nums) + 1.

# Revision Note:
# Important Bucket Sort pattern.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):

            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res