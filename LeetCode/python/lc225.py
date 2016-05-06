class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queueA = [];
        self.queueB = [];
        self.size = 0;
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """        
        if not self.queueA and not self.queueB:
            self.queueA.append(x);
        elif self.queueA and not self.queueB:
            self.queueB.append(x);
            for i in range(len(self.queueA)):
                tmp = self.queueA.pop(0);
                self.queueB.append(tmp);
        elif not self.queueA and self.queueB:
            self.queueA.append(x);
            for i in range(len(self.queueB)):
                tmp = self.queueB.pop(0);
                self.queueA.append(tmp);
        
        self.size += 1;


        

    def pop(self):
        """
        :rtype: nothing
        """
        
        if self.size > 0:
            if self.queueA and not self.queueB:
                self.queueA.pop(0);
            elif not self.queueA and self.queueB:
                self.queueB.pop(0);
        self.size -= 1;
        

    def top(self):
        """
        :rtype: int
        """
        if self.size > 0:
            if self.queueA and not self.queueB:
                return self.queueA[0];
            elif not self.queueA and self.queueB:
                return self.queueB[0];
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True;
        else:
            return False;