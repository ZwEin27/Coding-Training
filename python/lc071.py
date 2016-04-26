class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        elements = path.split('/')
        print elements

        ans = []
        for element in elements:
            if element == '' or element == '.':
                continue
            if element == '..':
                if len(ans):
                    ans.pop(-1)
                    continue
                else:
                    continue
            ans.append(element)

        return '/' + '/'.join(ans)


path = "/a/./b/../../c/"
print Solution().simplifyPath(path)
