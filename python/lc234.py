# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        size = 0;
        cur = head;
        while cur != None:
            size += 1;
            cur = cur.next;

        half_pos = size / 2;
        cur = head;
        for i in range(half_pos):
            cur = cur.next;
        if size%2 != 0:
            cur = cur.next;
        mid = self.reverseList(cur);

        curA = head;
        curB = mid;
        while curB != None:
            if curA.val != curB.val:
                return False;
            curA = curA.next;
            curB = curB.next;
        return True;


    def reverseList(self, head):
        if head == None:
            return head;
        header = head;
        cur = head.next;
        while cur != None:
            head.next = cur.next;
            cur.next = header;
            header = cur;
            cur = head.next;
        return header;


