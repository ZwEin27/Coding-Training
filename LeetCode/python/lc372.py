class Solution(object):
    # https://www.hrwhisper.me/leetcode-super-pow/
    # https://discuss.leetcode.com/topic/50489/c-clean-and-short-solution
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        m = 1337
        n = len(b)
        ans = 1
        for x in b[::-1]:
            ans = ans*self.quick_pow(a, x, m) % m
            a = self.quick_pow(a, 10, m)
        return ans

    def quick_pow(self, a, b, n):
        # http://www.jiuzhang.com/solutions/fast-power/
        ans = 1
        while b > 0:
            if b % 2==1:
                ans = ans * a % n
            a = a * a % n
            b = b / 2
        return ans % n
