class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bcode = set()
        for i in range(len(s) - k + 1):
            bcode.add(s[i : i + k])
        
        return len(bcode) == 2**k
    
    # time complexity: O(n)
    # space complexity: O(2^k)