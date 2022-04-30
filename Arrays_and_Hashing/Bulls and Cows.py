class Solution(object):
    def getHint(self, secret, guess):
        initial_len = len(secret)
        secret = list(secret)
        guess = list(guess)
        to_be_removed = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                to_be_removed.append(secret[i])

        for i in range(len(secret)):
            if secret[i] in guess:
                guess.remove(secret[i])

        bulls = len(to_be_removed)
        cows = initial_len - len(guess) - len(to_be_removed)
        return(str(bulls)+"A"+str(cows)+"B")
