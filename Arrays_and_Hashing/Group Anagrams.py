class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}
        for string in strs:
            if ''.join(sorted(string)) not in dict:
                dict[''.join(sorted(string))] = [string]
            else:
                dict[''.join(sorted(string))].append(string)
        return dict.values()
