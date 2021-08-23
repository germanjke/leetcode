class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            
            diff = target - n
            #diff = 9 - 2 = 7
            #diff = 9 - 7 = 2
            
            if diff in d:
                return [i, d[diff]]
            
            else:
                d[n] = i
                #d[0] = 2
            
        return []
