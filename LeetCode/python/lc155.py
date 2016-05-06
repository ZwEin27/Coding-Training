class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [];
        self.stack_min = [];
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x);
        if len(self.stack_min) == 0 or min(self.stack_min) >= x:    # need min
            self.stack_min.append(x);
        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.stack) > 0:
            tmp = self.stack.pop();
            if tmp == self.stack_min[len(self.stack_min) - 1]:
                self.stack_min.pop();
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1];
        return 0;
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack_min:
            return 0;
        return self.stack_min[len(self.stack_min) - 1];
        