# http://blog.csdn.net/xyqzki/article/details/50127749
# http://blog.csdn.net/xyqzki/article/details/50127749
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        sun_list = [1]  # 1 is a super ugly number for any given primes
        k2 = k3 = k5 = 0
        while len(sun_list) < n:
            a, b, c = sun_list[k2]*2, sun_list[k3]*3, sun_list[k5]*5
            m = min([a, b, c])
            if m == a:
                k2 += 1
            if m == b:
                k3 += 1
            if m == c:
                k5 += 1
            sun_list.append(m)
        return sun_list[-1]