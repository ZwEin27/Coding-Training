class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # http://blog.csdn.net/xiaobaohe/article/details/7897966
        
        return self.csum(0, candidates, target)

    def csum(self, cur, candidates, target):
        clen = len(candidates)
        result = []
        if cur > target:
            return result
        for i in range(clen):
            tmp = cur + candidates[i]
            if tmp == target:
                result.append([candidates[i]])
            else:
                ans = self.csum(tmp, candidates[i:], target)
                if ans != []:
                    for aitem in ans:
                        aitem.insert(0, candidates[i])
                        aitem.sort()
                        result.append(aitem)
        result.sort()
        return result

