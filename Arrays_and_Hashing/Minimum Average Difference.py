class Solution(object):
    def minimumAverageDifference(self, nums):
        min_avg_dif_index = 0
        all_sum = sum(nums)
        min_avg_dif = all_sum
        length = len(nums)
        counter = 1
        sum_counter = 0
        for i in range(1,len(nums)):
            sum_counter += nums[i-1]
            avg_dif = abs(int(sum_counter/counter) - int((all_sum-sum_counter)/(length - counter)))
            if avg_dif < min_avg_dif:
                min_avg_dif = avg_dif
                min_avg_dif_index = i-1
            counter+=1
        if int(sum(nums)/len(nums)) <  min_avg_dif:
            min_avg_dif_index = len(nums) - 1
        return(min_avg_dif_index)
