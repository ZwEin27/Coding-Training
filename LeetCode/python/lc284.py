# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache_next = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cache_next:
            return self.cache_next

        if self.hasNext():
            self.cache_next = self.iterator.next()
            return self.cache_next


    def next(self):
        """
        :rtype: int
        """
        if self.cache_next:
            tmp = self.cache_next
            self.cache_next = None
            return tmp
        else:
            return self.iterator.next()


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iterator.hasNext() or self.cache_next:
            return True
        return False


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].