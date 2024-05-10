#The first soltion that came into my mind
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()

        if list_s == list_t:
            return True
        else:
            return False

#A new approach that is not efficient than the above code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
