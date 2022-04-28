class Solution(object):
    def longestCommonPrefix(self, strs):
        smallest = len(strs[0])
        for word in strs:
            if len(word) < smallest:
                smallest = len(word)

        longest_prefix = ""
        for i in range(smallest):
            prefix = strs[0][:i+1]
            flag = True
            for word in strs:
                if prefix != word[:i+1]:
                    flag = False
            if flag:
                longest_prefix = prefix
            else:
                break

        return(longest_prefix)
