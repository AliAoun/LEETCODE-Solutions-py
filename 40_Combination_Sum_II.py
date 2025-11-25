class Solution:
    def combinationSum2 (self, candidates: List[int], target: int) -> List [List[int]]:
        candidates.sort()
        res = []
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res
    
    # Time Complexity: O(2^n) in the worst case, where n is the number of candidates.
    # Space Complexity: O(n) for the recursion stack and the current combination list.