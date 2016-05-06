class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")

        ht = {}
        slen = len(str)
        plen = len(pattern)
        for i in range(plen):
            cur_pattern = pattern[i]
            ht.setdefault(cur_pattern, [])
            ht[cur_pattern].append(i)
        print ht

        if slen != plen:
            return False

        appeared_list = []
        for (k, v) in ht.items():
            tmp = ""
            for index in v:
                if index >= slen:
                    return False
                if tmp == "":
                    tmp = str[index]
                    if tmp in appeared_list:
                        return False
                else:
                    if tmp != str[index]:
                        return False
            appeared_list.append(tmp)

        return True