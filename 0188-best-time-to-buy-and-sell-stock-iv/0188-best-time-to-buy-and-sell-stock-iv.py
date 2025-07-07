class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ahead = [[0] * (k + 1) for _ in range(2)]
        cur = [[0] * (k + 1) for _ in range(2)]
        n=len(prices)
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):

                    if buy == 0: 
                        cur[buy][cap] = max(0 + ahead[0][cap],
                                        -prices[ind] + ahead[1][cap])
                    if buy == 1: 
                        cur[buy][cap] = max(0 + ahead[1][cap],
                                        prices[ind] + ahead[0][cap - 1])
            ahead = cur.copy()

        return ahead[0][k]
            