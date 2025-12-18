from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):
            # Append a copy of current subset
            res.append(path[:])

            for i in range(start, len(nums)):
                # Skip duplicates at this level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i]
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res