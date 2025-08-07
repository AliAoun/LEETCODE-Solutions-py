class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maxSW = []
        # for i in range(len(nums) - k + 1):
        #     maxSW.append(max(nums[i: i + k]))
        # return maxSW

        # l, r = 0, k - 1
        # while r < len(nums):
        #     maxSW.append(max(nums[l: l + k]))
        #     l += 1
        #     r += 1
        # return maxSW

        maxSW = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                maxSW.append(nums[q[0]])
                l += 1
            r += 1
        return maxSW
    
    # time complexity: O(n)
    # space complexity: O(k)