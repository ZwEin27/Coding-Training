# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        cur = head
        pre = head
        while cur != None and cur.next != None:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = cur
            if cur == head:
                head = nxt
            else:
                pre.next = nxt
            pre = cur
            cur = cur.next
        return head