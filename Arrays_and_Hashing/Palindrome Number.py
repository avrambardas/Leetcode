class Solution(object):
    def isPalindrome(self, x):
        if list(str(x)) == list(str(x))[::-1]:
            return True
        return False
