class Solution(object):
    def romanToInt(self, s):
        roman_values = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        answer = 0
        prev = 0

        for char in reversed(s):
            current_value = roman_values[char]
            
            if current_value < prev:
                answer -= current_value
            else:
                answer += current_value
            
            prev = current_value

        return answer

# 12 ms
# Also easier to interpret and I prefer this one other than the other one since it is also faster.
