# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k

#         def quickSelect(l, r):
#             pivot, p = nums[r], l
#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]

#             if p > k:   return quickSelect(l, p - 1)
#             elif p < k: return quickSelect(p + 1, r
#             else:       return nums[p]
        
#         return quickSelect(0, len(nums) - 1)

##### Time exceed in that previous solution, below is the optimized one #####

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
    
    # Time Complexity: O(N log k) as we process N elements and each insertion/deletion in the heap takes O(log k) time.
    # Space Complexity: O(k) as we are using a heap of size k.