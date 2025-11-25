class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
    
    # Time Complexity: O(N * 2^N) where N is the length of nums. Due to sorting and generating all subsets.
    # Space Complexity: O(N) for the recursion stack and subset storage.