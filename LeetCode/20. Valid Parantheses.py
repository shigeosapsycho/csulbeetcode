class Solution(object):
    def isValid(self, s):
        stack = [] # Create an empty stack

        for char in s:
                if char == '(' or char == '[' or char == '{': # If the character is an opening bracket, push it to the stack
                    stack.append(char)
                elif char == ')' and stack and stack[-1] == '(': # If the character is a closing bracket, check if the stack is empty and if the top of the stack is the corresponding opening bracket
                    stack.pop()
                elif char == ']' and stack and stack[-1] == '[': # If the character is a closing bracket, check if the stack is empty and if the top of the stack is the corresponding opening bracket
                    stack.pop()
                elif char == '}' and stack and stack[-1] == '{': # If the character is a closing bracket, check if the stack is empty and if the top of the stack is the corresponding opening bracket
                    stack.pop() # If the conditions are met, pop the top of the stack
                else:
                    return False # If the conditions are not met, return False
        return len(stack) == 0 # If the stack is empty, then the string is valid. Otherwise, it is not. Outputting True
    
# O(n) time complexity

"""
solution = Solution()

# Test Case: - What is happening in that test case?
print(solution.isValid("()"))
 - The stack is initalized as an empty stack (stack = []) so now it will look through the characters in the string "()".
 - The first character in the string '(' meets line 6's condition that the character is an opening bracket, so it will push the character to the stack. The stack is now ['('].
 - The function continues looping through the string. The next character is ')'. The function checks if the character is a 
 closing paranthesis and if the stack is not empty, and the top of the stack (stack[-1]) is a matching opeiing paranthesis. '('.
 The condition is met in line 9: elif char == ')' and stack and stack[-1] == '(': so the stack is popped to remove the matching '('. After popping, the stack becomes empty again
 - After procesing all the characters, the len(stack) is 0 so it returns True. If there is still a missing pair in the stack, it would return False.
"""