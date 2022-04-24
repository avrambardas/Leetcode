class Solution(object):
    def isAnagram(self, s, t):
        string1 = sorted(list(s))
        string2 = sorted(list(t))
        if "".join(string1) == "".join(string2):
            return True
        return False
