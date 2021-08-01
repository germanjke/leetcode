class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_, sum_ = max(milestones), sum(milestones)
        if (sum_ - max_) >= max_:
            return sum_
        else:
            return 2 * (sum_ - max_) + 1
