# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # the longer list goes first, and go (h1 - h2) steps
        lenA = self.countListLength(headA);
        lenB = self.countListLength(headB);
        curA = headA;
        curB = headB;
        for i in range(0, abs(lenA - lenB)):
            if len1 >= len2:
                curA = curA.next;
            else:
                curB = curB.next;

        while curA != None and curB != None:
            if curA.val == curB.val:
                return curA;
            else:
                curA = curA.next;
                curB = curB.next;

        return null;


    def countListLength(self, list_head):
        cur = list_head;
        length = 0;
        while cur != None:
            length += 1;
            cur = cur.next;
        return length;

