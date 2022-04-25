class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        s = list(s)

        max1 = 0
        counter = 0
        i = 0
        start = 0
        while i < len(s):
            if s[i] not in s[start:i]:
                counter += 1
                if counter > max1:
                    max1 = counter
                i+=1
            else:
                j = i-1
                while s[j] != s[i]:
                    j -=1
                i = j+1
                start = i
                counter = 0
        return(max1)
