class Solution(object):
    def containsDuplicate(self, nums):
        existing = set(nums)
        if len(nums) == len(existing):
            return False
        return True
