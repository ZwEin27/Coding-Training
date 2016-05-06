class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        S1 = abs(A-C) * abs(B-D);
        S2 = abs(E-G) * abs(F-H);
        #more = abs(r1 - r2);
        S1N2 = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0);
        return S1 + S2 - S1N2;

        