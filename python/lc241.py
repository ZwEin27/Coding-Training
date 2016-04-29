# http://bookshadow.com/weblog/2015/07/27/leetcode-different-ways-add-parentheses/

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re
        def cal(a, b, o):
            return {'+': lambda x, y: x+y,
                    '-': lambda x, y: x-y,
                    '*': lambda x, y: x*y
                    }[o](a, b)

        def dfs(nums, ops):
            if not ops:
                return [nums[0]]
            ans = []
            for i in range(len(ops)):
                left = dfs(nums[:i+1], ops[:i])
                right = dfs(nums[i+1:], ops[i+1:])
                for l in left:
                    for r in right:
                        ans.append(cal(l, r, ops[i]))
            return ans


        input = re.split('(\D)', input)
        nums = []
        ops = []
        for v in input:
            if v.isdigit():
                nums.append(int(v))
            else:
                ops.append(v)
        return dfs(nums, ops)

ipt = '2-1-1'
print Solution().diffWaysToCompute(ipt)
