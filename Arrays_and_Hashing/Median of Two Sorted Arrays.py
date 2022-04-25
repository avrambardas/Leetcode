class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        p1 = 0
        p2 = 0
        merged = []
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1+=1
            else:
                merged.append(nums2[p2])
                p2+=1

        if p1>=len(nums1):
            [merged.append(nums2[i]) for i in range(p2, len(nums2))]
        else:
            [merged.append(nums1[i]) for i in range(p1, len(nums1))]

        if len(merged)%2==0:
            floor = int(len(merged)/2-1)
            return((merged[floor]+merged[floor+1])/2.0)
        else:
            return(merged[int(len(merged)/2)])
