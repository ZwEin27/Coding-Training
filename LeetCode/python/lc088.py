class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
       

        n1len = len(nums1);
        for i in range(m, n1len):
            nums1.pop();

        print nums1

        i1 = 0;
        i2 = 0;
        while i1 < m:
            while i2 < n:
                if nums1[i1] >= nums2[i2]:
                    nums1.insert(i1, nums2[i2]);
                    i1 += 1;
                    m += 1;
                else:
                    break;
                i2 += 1;
            i1 += 1;


        for i2 in range (i2, n):
            nums1.append(nums2[i2]);