class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # A dictionary that maps roman numerals to integers

        result = 0 # The result of the conversion
        
        for value in range(len(s)):
            if value > 0 and roman[s[value]] > roman[s[value - 1]]:
                result += roman[s[value]] - 2 * roman[s[value - 1]]
            else:
                result += roman[s[value]]
        return result
    
# Time Complexity is O(n) where n is the length of the input string
# Runtime is 15 ms (BEST CASE)
