class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set(nums)
        
        if len(nums) > len(set_):
            return True
        
        else:
            return False
