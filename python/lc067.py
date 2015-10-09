class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alen = len(a);
        blen = len(b);
        i = 0;
        si = 0;
        flag = 0;
        result = "";
        while 1:
            ai = alen - 1 - i;
            bi = blen - 1 - i;
            if i >= alen and i < blen:  # >= and < is important
                si = int(b[bi]) + flag;
            elif i < alen and i >= blen:
                si = int(a[ai]) + flag;
            elif i < alen and i < blen:
                si = int(a[ai]) + int(b[bi]) + flag;
            else:
                print i
                # si = flag;
                # result = str(si%2) + result;
                break;
            result = str(si%2) + result;
            # if i == alen or i == blen:
            #     break;
            if flag == 1:
                flag = 0;
            if si >= 2:
                flag = 1;
            
            i += 1;
        if flag == 1:
            result = '1' + result; 
        return result;