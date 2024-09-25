class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0: # checks if it is a not a power of 2, powers of 2 must be a positive integer
            return False
        return n & (n - 1) == 0 
    
# 21 ms
