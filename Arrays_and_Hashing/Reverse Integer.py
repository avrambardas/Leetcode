class Solution(object):
    def reverse(self, x):
        if x>=0:
            x = int("".join(list(str(x))[::-1]))
        else:
            x = int("".join(list(str(x))[::-1])[:-1])*(-1)
            
        if x <-2**31 or x>2**31-1:
            return 0
        return x
