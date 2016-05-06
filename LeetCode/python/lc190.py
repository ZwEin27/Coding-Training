"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = bin(n);
        #print bits
        strbits = str(bits);
        #print strbits
        strbits = strbits[2:];
        

        strbits = strbits[::-1];
        #print strbits
        
        if len(strbits) < 32:
            gap = 32 - len(strbits);
            while gap > 0:
                strbits += '0';
                gap -= 1;
        strbits = "0b" + strbits;
        #print strbits
        return int(strbits, 2)
        #return strbits