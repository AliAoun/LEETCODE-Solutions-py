class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def cn(n,b): 
            d=[] 
            while n: 
                d.append(n%b) 
                n//=b 
            return d[::-1]
        
        def isP(x): 
            return x==x[::-1] 
        
        for b in range(2,n-1): 
            c=cn(n,b) 
            if not isP(c): 
                return False 
        
        return True 
    
    # Time Complexity: O(n^2) due to the nested loop and the palindrome check. Because we are checking for all bases from 2 to n-2, and for each base, we are converting the number to that base and checking if it's a palindrome, which takes O(n) time in the worst case.
    # Space Complexity: O(n) for the list used to store the digits in base b.