class Solution(object):
    def addBinary(self, a, b):
        addition = int(a, 2) + int(b, 2) # take a and b with the integer function with base 2
        return bin(addition)[2:] # convert the result of line 3 and then slice off the first two because it will always return 0b####
    
# 9 ms !!!
# easiest leetcode problem I have ever done
