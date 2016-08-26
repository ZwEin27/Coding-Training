class Solution(object):
    """
    One knowledge: ab % k = (a%k)(b%k)%k
    Since the power here is an array, we'd better handle it digit by digit.
    One observation:
    a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
    Looks complicated? Let me put it other way:
    Suppose f(a, b) calculates a^b % k; Then translate above formula to using f :
    f(a,1234567) = f(a, 1234560) * f(a, 7) % k = f(f(a, 123456),10) * f(a,7)%k;
    """
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
