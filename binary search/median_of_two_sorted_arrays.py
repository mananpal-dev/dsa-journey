# Problem: Median of Two Sorted Arrays
# Platform: LeetCode
# Difficulty: Hard

# Approach:
# Use Binary Search on the smaller array.
#
# Partition both arrays such that:
# Left half contains exactly half of the elements.
#
# A valid partition satisfies:
#
# max_left1 <= min_right2
# max_left2 <= min_right1
#
# Once a valid partition is found:
# - Odd total length:
#     median = max(left side)
#
# - Even total length:
#     median = average of
#     max(left side) and min(right side)

# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

# Common Mistake:
# Performing binary search on the larger array.
# Always binary search on the smaller array.

# Revision Note:
# Partition-Based Binary Search.
#
# Goal:
# Left side and right side should be perfectly balanced.

class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len1, len2 = len(nums1), len(nums2)

        left = 0
        right = len1

        while left <= right:

            part1 = (left + right) // 2
            part2 = (len1 + len2 + 1) // 2 - part1

            max_left1 = (
                float('-inf')
                if part1 == 0
                else nums1[part1 - 1]
            )

            min_right1 = (
                float('inf')
                if part1 == len1
                else nums1[part1]
            )

            max_left2 = (
                float('-inf')
                if part2 == 0
                else nums2[part2 - 1]
            )

            min_right2 = (
                float('inf')
                if part2 == len2
                else nums2[part2]
            )

            if (
                max_left1 <= min_right2
                and
                max_left2 <= min_right1
            ):

                if (len1 + len2) % 2 == 0:

                    return (
                        max(max_left1, max_left2)
                        +
                        min(min_right1, min_right2)
                    ) / 2

                else:

                    return max(max_left1, max_left2)

            elif max_left1 > min_right2:

                right = part1 - 1

            else:

                left = part1 + 1