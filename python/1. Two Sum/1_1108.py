class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in d.keys():
                d[diff] = i
            else:
                return [d[nums[i]], i]
