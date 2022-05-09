class Solution(object):
    def isMonotonic(self, nums):
        if nums[0] < nums[-1]:
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i]:
                    return False
        return True
