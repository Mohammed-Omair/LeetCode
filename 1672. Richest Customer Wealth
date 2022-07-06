class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumofaccounts = []
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum = sum + accounts[i][j]
            sumofaccounts.append(sum)
        return max(sumofaccounts)
