#!/usr/bin/env python

# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        pspan = n - 1;
        result = head;
        target = head;
        pret = target;
        cur = head;
        while 1:
            if cur.next == None:
                # remove target
                pret.next = target.next;
                if target == head:
                    result = target.next;
                break;
            if pspan == 0:
                pret = target;
                target = target.next;
            else:
                pspan = pspan - 1;
            cur = cur.next;

        return result;