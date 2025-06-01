class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ToDo: Write Your Code Here.
        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        for j in range(len(s)):
            if hm[s[j]] == 1:
                return j
        return -1

