# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        pipe = []
        tmp = head
        while tmp:
            pipe.append(tmp)
            tmp = tmp.next

        print len(pipe)
        order_flag = False
        pre = None
        while pipe:
            if not pre:
                pre = pipe.pop(0)
                pre.next = None
            else:
                if order_flag:
                    cur = pipe.pop(0)
                    order_flag = False
                else:
                    cur = pipe.pop(-1)
                    order_flag = True
                cur.next = None
                pre.next = cur
                pre = cur
