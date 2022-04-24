class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                target -= nums[i]
                index = i
                break
                
        for i in range(len(nums)):
            if nums[i] == target and i != index:
                return [index, i]
