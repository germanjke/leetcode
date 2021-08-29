class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans, dp = 0, 0
        for i in range(0, len(prices)-1):
            q = prices[i+1] - prices[i]
            dp = max(dp + q, q)
            ans = max(ans, dp)
            
            print(f'q:{q}')
            print(f'dp:{dp}')
            print(f'ans:{ans}')
        return ans
