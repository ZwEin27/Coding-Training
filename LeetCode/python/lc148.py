"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        if not head:
            return
        sorted_value = []
        tmp = head
        while tmp:
            sorted_value.append(tmp.val)
            tmp = tmp.next
        sorted_value.sort()

        tmp = head
        for value in sorted_value:
            tmp.val = value
            tmp = tmp.next
        return head
        
