#URL: https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        for i in split_path:
            print(i)
            if i == "..":
                if stack:
                    stack.pop()
            elif not i or i == ".":
                continue
            else:
                stack.append(i)
        result = "/" + "/".join(stack)
        return result
        
