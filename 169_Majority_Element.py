class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n                          # Time Complexity: O(n) Space Complexity: O(1)
            count += (1 if n == res else -1)
        return res
    



        # count = {}
        # res, maxCount = 0, 0
        
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > maxCount else res       # Time Complexity: O(n) Space Complexity: O(n)
        #     maxCount = max(count[n], maxCount)
        # return res