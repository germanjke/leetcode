from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            
        
        for k, v in d.items():
            if v > 1:
                return True
            
        return False
