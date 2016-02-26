
# http://blog.csdn.net/xyqzki/article/details/50379007

import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        length = len(primes)
        sun_list = [1]  # 1 is a super ugly number for any given primes
        idx = [0] * length
        minlist = [(primes[i] * sun_list[idx[i]], i) for i in range(length)]
        heapq.heapify(minlist)
        while len(sun_list) < n:
            min_item, min_idx = heapq.heappop(minlist)
            idx[min_idx] += 1
            if min_item != sun_list[-1]:
                sun_list.append(min_item)
            heapq.heappush(minlist, (primes[min_idx] * sun_list[idx[min_idx]], min_idx))
        return sun_list[-1]

