class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k - 1
        res = float("inf")
        nums.sort()

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res
    
    # time complexity: O(n log n) due to sorting
    # space complexity: O(1) since we are using constant space for variables