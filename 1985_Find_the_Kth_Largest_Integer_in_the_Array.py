class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-int(n) for n in nums]
        heapq.heapify(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        return str(-maxHeap[0])
    
    # Time Complexity: O(N + klogN) where N is the number of elements in nums and k is the given integer. As we are
    # using a heap to store all the elements, it takes O(N) time to build the heap. Then we are popping k-1 elements from the heap,
    # each pop operation takes O(logN) time.

    # Space Complexity: O(N) as we are using a heap to store all the elements from nums.