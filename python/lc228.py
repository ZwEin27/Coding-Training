class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # http://www.tuicool.com/articles/J32Ury
        result = [];
        idx, size = 0, len(nums);
        while idx < size:
            cidx = idx;
            cnum = str(nums[idx]);
            while idx + 1 < size and nums[idx+1] - 1 == nums[idx]:
                idx += 1;
            if idx > cidx:
                cnum += "->" + str(nums[idx]);
            result.append(cnum);
            idx += 1;
        return result;


