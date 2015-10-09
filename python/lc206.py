# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self):
        self.next_node = None;
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iteratively
        """
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
        """
        # recursively
        if head == None:
            return head;


        lt = self.reverseList(head.next);
        if lt != None:
            # cur = lt;
            # while cur.next != None:
            #     cur = cur.next;
            if not self.next_node:
                self.next_node = lt;
            self.next_node.next = head;
            self.next_node = head;
            head.next = None;
            return lt;
        else:
            return head;
        



