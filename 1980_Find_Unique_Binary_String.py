class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strset = { s for s in nums }

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strset else res

            res = backtrack(i + 1, cur)
            if res:
                return res
                
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res: 
                return res
                
        return backtrack(0, ["0" for s in nums])
    
    # time complexity: O(n * 2^n)
    # space complexity: O(n)