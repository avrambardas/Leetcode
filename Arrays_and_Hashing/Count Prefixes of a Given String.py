class Solution(object):
    def countPrefixes(self, words, s):
        counter = 0
        for word in words:
            if word == s[:len(word)]:
                counter += 1
        return counter
