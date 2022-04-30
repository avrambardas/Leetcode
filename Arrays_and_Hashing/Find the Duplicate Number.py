class Solution(object):
    def findDuplicate(self, nums):
        s = set()
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)
