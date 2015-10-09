#!/usr/bin/env python

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        
        if not l1 and not l2:
            return [];
        elif not l1 and l2:
            return l2;
        elif l1 and not l2:
            return l1;

        result = [];

        if l1.val <= l2.val:
            result = l1;
            result.next = self.mergeTwoLists(l1.next, l2);
        elif l1.val > l2.val:
            result = l2;
            result.next = self.mergeTwoLists(l1, l2.next);

        return result;


        