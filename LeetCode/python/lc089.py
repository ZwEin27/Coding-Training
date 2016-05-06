class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return [0]
        ret = [0, 1]
        for i in range(1, n):
            size = len(ret)
            tmp = []
            tmp.extend(ret)
            cur = 1 << i
            for j in range(size):
                tmp.append(cur + ret[size-1-j])
            ret = tmp
        return ret
