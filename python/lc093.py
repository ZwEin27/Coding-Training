class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.func(s, [], ans)
        return ans

    def is_valid(self, num_string):
        length = len(num_string)
        num = int(num_string)
        if length == 1 and num >= 0 and num <= 9:
            return True
        if length == 2 and num >= 10 and num <= 99:
            return True
        if length == 3 and num >= 100 and num <= 255:
            return True
        return False


    def func(self, s, ip, ans):

        if len(ip) == 4:
            if not s:
                ans.append('.'.join(ip))
            pass
        elif len(ip) > 4:
            # print ip
            pass
        else:
            if not s:
                pass
            else:
                for i in range(1,4):

                    if len(s[:i]) != i or not self.is_valid(s[:i]):
                        continue

                    # if i == 3 and int(s[:i]) > 255:
                    #     continue
                    # print s[:i]
                    # print i, s, s[:i], ip, ans, len(s[:i])
                    new_ip = list(ip)
                    new_ip.append(s[:i])
                    self.func(s[i:], new_ip, ans)

s = "010010"
print Solution().restoreIpAddresses(s)
