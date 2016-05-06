class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        # clen = len(candidates)
        # for i in range(clen):
        #     if candidates[i] > target:
        #         continue
        #     if candidates[i] == target:
        #         result.append([ci])
        #     if candidates[i] < target:
        #         ans = self.combinationSum2(candidates[i:], target)
        #         if ans != []:
        result = self.csum(0, candidates, target)

        result_nodup = []
        for item in result:
            if item not in result_nodup:
                result_nodup.append(item)

        return result_nodup



    def csum(self, cur_sum, candidates, target):
        clen = len(candidates)
        result = []

        if cur_sum > target:
            return result

        for i in range(clen):
            tmp = cur_sum + candidates[i]
            if tmp > target:
                continue

            if tmp == target:
                result.append([candidates[i]])
            else:
                if i == clen - 1:
                    break
                ans = self.csum(tmp, candidates[i+1:], target)
                if ans != []:
                    for aitem in ans:
                        aitem.insert(0, candidates[i])
                        aitem.sort()
                        result.append(aitem)
        result.sort()
        return result