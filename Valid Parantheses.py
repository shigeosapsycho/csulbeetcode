class Solution(object):
    def isValid(self, s):
        stack = [] # Create an empty stack

        for char in s:
                if char == '(' or char == '[' or char == '{':
                    stack.append(char)
                elif char == ')' and stack and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 # If the stack is empty, then the string is valid. Otherwise, it is not. Outputting True
    
# 17 ms O(n) time complexity
