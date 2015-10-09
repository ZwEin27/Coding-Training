# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None;
        pre = head;
        cur = pre.next;
        while cur != None:
            if pre.val == cur.val:
                if cur.next != None:
                    pre.next = cur.next;
                    cur = cur.next;
                    continue;
                else:
                    pre.next = None;
                    return head;
                #del cur;
            pre = cur;
            cur = cur.next;
        return head;