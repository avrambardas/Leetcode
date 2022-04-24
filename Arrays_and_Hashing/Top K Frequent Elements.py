class Solution(object):
    def topKFrequent(self, nums, k):
        set_num = set(nums)
        print(set_num)
        counts = []
        for num in set_num:
            counts.append(nums.count(num))

        print(counts)
        Z = [x for _,x in sorted(zip(counts,set_num), reverse=True)]
        return Z[:k]
