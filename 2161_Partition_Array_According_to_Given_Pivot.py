class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivotCount = 0
        leftAry = []
        rightAry = []
        for i in range(len(nums)):
            if nums[i] == pivot:
                pivotCount += 1
            elif nums[i] < pivot:
                leftAry.append(nums[i])
            else:
                rightAry.append(nums[i])
        return leftAry + [pivot] * pivotCount + rightAry
    
    # time complexity: O(n)
    # space complexity: O(n) 

