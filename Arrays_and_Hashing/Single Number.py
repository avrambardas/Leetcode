class Solution(object):
    def singleNumber(self, nums):
        setted = set(nums)
        return (sum(setted)*2 - sum(nums))
        
