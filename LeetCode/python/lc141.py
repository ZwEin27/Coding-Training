# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False

        fast = head.next
        slow = head

        while fast != None and fast.next != None:   # judge fast.next != None, since that we don't want fast -> Null -> Next
            if fast.val == slow. val:
                return True

            fast = fast.next.next
            slow = slow.next

        return False