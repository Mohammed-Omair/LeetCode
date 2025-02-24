#URL: https://leetcode.com/problems/kth-missing-positive-number/
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingNumbers = []
        # TODO: Write your code here
        i = 0
        n = len(arr)
        extraNumbers=[]
        while i < n:
            if arr[i] == i+1 or arr[i] < 1 or arr[i] > n:
                i += 1
            else:
                j = arr[i]
                if arr[j-1] == j:
                    i += 1
                else:
                    arr [i], arr[j-1] = arr[j-1], arr[i]
        i = 0
        while i < n and k != 0:
            if arr[i] != i+1:
                missingNumbers.append(i+1)
                extraNumbers.append(arr[i])
                k = k - 1
                i += 1
            else:
                i += 1
        j = 1
        while k != 0:
            if n+j not in extraNumbers:
                missingNumbers.append(n + j)
                k = k-1
            j += 1
        return missingNumbers[-1]
        
