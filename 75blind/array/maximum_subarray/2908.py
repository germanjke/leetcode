class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_best = float('-inf')
        ans = float('-inf')
        
        for num in nums:
            curr_best = max(curr_best + num, num)
            ans = max(curr_best, ans)
            
        return ans
