#URL:leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i in {"{", "[", "("}:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                if top == "{" and i != "}":
                    return False
                
                if top == "[" and i != "]":
                    return False

                if top == "(" and i != ")":
                    return False
        

        return not stack
