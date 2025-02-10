class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Empty list
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } # Dictionary to map the closed parantheses to open

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False # If the stack is empty it will return true, else return false if there is a missing pair.
