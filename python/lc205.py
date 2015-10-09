class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ht = {};
        strlen = len(s);
        for i in range(0, strlen):
            schr = s[i];
            tchr = t[i];
            ints = ord(schr);
            intt = ord(tchr);
            # print schr
            # print tchr

            if not ht.has_key(ints):
                for d,x in ht.items():
                    if x == intt:
                        return False;
                #if not ht.has_key(intt):
                ht[ints] = intt;
                #else:
                #    return False;
            else:
                if ht[ints] != intt:
                    return False;
            # print ht
        

        return True;