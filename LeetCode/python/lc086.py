# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # if not head:
        #     return []

        lx = None
        lx_head = None
        sx = None
        sx_head = None
        cur = head
        while cur != None:
            # print cur.val
            if cur.val < x:
                if sx:
                    sx.next = cur
                    sx = cur
                else:
                    sx_head = cur
                    sx = cur
               
                    
            else:
                if lx:
                    lx.next = cur
                    lx = cur
                else:
                    lx = cur
                    lx_head = lx
            cur = cur.next

        #  important  #
        if sx:
            sx.next = None
        if lx:
            lx.next = None
        ###############
        
        if sx:
            print sx.val
            sx.next = lx_head
            return sx_head
        if lx:
            print lx.val
            return lx_head

        return None
