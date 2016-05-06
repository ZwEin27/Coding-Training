class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackA = [];
        self.stackB = [];
        self.size = 0;
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stackA and not self.stackB:
            self.stackB.append(x);
        # elif self.stackA and not self.stackB:
            # self.stackB.append(x);
            # for i in range(len(self.stackA)):
            #     tmp = self.stackA.pop();
            #     self.stackB.append(tmp);
        elif not self.stackA and self.stackB:
            for i in range(len(self.stackB)):
                tmp = self.stackB.pop();
                self.stackA.append(tmp);
            self.stackA.append(x);
            for i in range(len(self.stackA)):
                tmp = self.stackA.pop();
                self.stackB.append(tmp);

            
        self.size += 1;

        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.size > 0:
            # if self.stackA and not self.stackB:
                # for i in range(len(self.stackA)):
                #     tmp = self.stackA.pop();
                #     self.stackB.append(tmp);
                #     self.stackB.pop();
            if not self.stackA and self.stackB:
                # for i in range(len(self.stackB)):
                #     tmp = self.stackB.pop();
                #     self.stackA.append(tmp);
                #     self.stackA.pop();
                self.stackB.pop();
            self.size -= 1;
        

    def peek(self):
        """
        :rtype: int
        """
        if self.size > 0:
            if not self.stackA and self.stackB:
                return self.stackB[self.size - 1];
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True;
        else:
            return False;
        