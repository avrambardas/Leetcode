class Solution(object):
    def moveZeroes(self, nums):
        counter = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                counter += 1
                nums.remove(nums[i])
            else:
                i += 1
                
        for i in range(counter):
            nums.append(0)
        return nums
