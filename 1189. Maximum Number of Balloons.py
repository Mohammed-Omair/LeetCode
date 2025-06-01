class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count = 0
        hm = {"b":0, "a":0, "l":0, "o":0, "n":0}
        # ToDo: Write Your Code Here.
        for i in text:
            if i in hm:
                hm[i] += 1
        minimum = min(hm.values())
        if hm["l"] >= 2*minimum and hm["o"] >= 2*minimum:
            min_count = min(hm.values())
        else:
            min_count = min(hm["l"], hm["o"])//2
        return min_count
