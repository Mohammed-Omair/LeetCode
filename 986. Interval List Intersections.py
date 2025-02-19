#URL: https://leetcode.com/problems/interval-list-intersections/
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            if (firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]) or (secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]):
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                result.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result
