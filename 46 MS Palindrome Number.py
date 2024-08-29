class Solution(object):
    def isPalindrome(self, x):
        x_str = [] if x < 0 else str(x)
        return ''.join(reversed(x_str)) == x_str

# 46 ms
