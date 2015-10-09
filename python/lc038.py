class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        tmp = "1";
        for i in range(0, n-1):
            tmp = self.cas(tmp);
        return tmp


    def cas(self, numseq):
        result = "";
        strlen = len(numseq);
        count = 1;
        pre = numseq[0];
        for i in range(1, strlen):
            cur = numseq[i];
            if pre == cur:
                count += 1;
            else:
                result += ("%d"%count + pre);
                count = 1;
            pre = cur;
        if count != 0:
            result += ("%d"%count + pre);
        return result;
