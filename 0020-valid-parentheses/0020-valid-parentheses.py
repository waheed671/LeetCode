class Solution:
    def isValid(self, s):
        stack = []
        close_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in close_map:  
                # If closing bracket, check top of stack
                if stack and stack[-1] == close_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket → push to stack
                stack.append(ch)

        return len(stack) == 0
