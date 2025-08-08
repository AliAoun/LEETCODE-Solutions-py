class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count


# time complexity: O(n^2) due to the nested loops iterating through the list.
# space complexity: O(1) due to the use of a constant amount of extra space for the count variable.