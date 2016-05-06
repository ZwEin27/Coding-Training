class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        length = len(secret)
        A = 0 # bulls
        B = 0 # cows
        list_s = []
        ht_g = {}

        for i in range(length):
            s = secret[i]
            g = guess[i]
            if s == g:
                A += 1
            else:
                list_s.append(s)
                ht_g.setdefault(g, 0)
                ht_g[g] += 1

        for i in list_s:
            if i in ht_g.keys() and ht_g[i] > 0:
                ht_g[i] -= 1
                B += 1

        return str(A) + 'A' + str(B) + 'B'
