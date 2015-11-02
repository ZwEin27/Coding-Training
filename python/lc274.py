class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        if size == 0:
            return 0
        citations.sort()
        print citations
        
        for i in range(size):
            tmp = size - i;
            if citations[i] >= tmp:
                return tmp;
        return 0

        
if __name__ == '__main__':
    s = Solution()
    print s.hIndex([3, 0, 6, 1, 5])