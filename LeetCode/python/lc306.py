class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        res = []
        self.dfs(num, [], res)
        return len(res) != 0

    def dfs(self, num, num_list, res):
        if not num:
            if len(num_list) <= 2:
                return
            res.append(num_list)
            return
        for i in range(1, len(num)+1):
            if len(num_list) > 1:
                if num_list[-1] + num_list[-2] != int(num[:i]):
                    continue
            if len(num[:i]) > 1 and num[:i][0] == '0':
                continue
            self.dfs(num[i:], num_list + [int(num[:i])], res)


num = '112358'
print Solution().isAdditiveNumber(num)







