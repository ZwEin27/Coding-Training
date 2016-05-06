class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s);
        tlen = len(t);
        ht = {};

        for i in range(min(slen, tlen)):
            ch = '';
            if tlen <= slen:
                ch = t[i];
            else:
                ch = s[i];
            if not ht.has_key(ch):
                ht[ch] = 1;
            else:
                ht[ch] += 1;


        for i in range(max(slen, tlen)):
            ch = '';
            if slen >= tlen:
                ch = s[i];
            else:
                ch = t[i];
            
            if not ht.has_key(ch):
                return False;
            else:
                if ht[ch] > 0:
                    ht[ch] -= 1;
                if ht[ch] == 0:
                    ht.pop(ch);
                #t_ht[ch] += 1;

        print ht.keys()
        print ht.values()
        if ht.keys():
            return False;
        return True;
