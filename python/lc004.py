#!/usr/bin/env python

# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

class Solution:


    # @return a float
    def findMedianSortedArrays(self, A, B):
        print 'A:', A, ' length:', len(A), '\n'
        print 'B:', B, ' length:', len(B), '\n'

        
        if len(A) == 0:
            (mb, mpb) = self.splitSetByMedian(B);
            return mb;

        if len(B) == 0:
            (ma, mpa) = self.splitSetByMedian(A);
            return ma;


        (ma, mpa) = self.splitSetByMedian(A);
        (mb, mpb) = self.splitSetByMedian(B);
        if len(A)<=2 and len(B)<=2:
            if ma>mb:
                return (min(A)+max(B))/2.0;
            elif ma<mb:
                return (max(A)+min(B))/2.0;
            else:
                return ma;
            
        print 'ma:', ma, ' mb:', mb, '\n'
        if ma > mb:
            if mpa==0:
                subA = A;
            else:
                subA = A[:mpa];
            if mpb==0:
                subB = B;
            else:
                subB = B[mpb:];
        elif ma < mb:
            if mpa==0:
                subA = A;
            else:
                subA = A[mpa:];
            if mpb==0:
                subB = B;
            else:
                subB = B[:mpb];
        else:
            return ma;

        return self.findMedianSortedArrays(subA, subB);



    def splitSetByMedian(self, set):
        length = len(set);

        median = 0;
        median_pos = 0;
        if length%2 == 0:
            median_pos = length/2;
            median = (set[median_pos-1] + set[median_pos])/2.0;
        else:
            median_pos = length/2;
            median = set[median_pos];
        return (median, median_pos);

    