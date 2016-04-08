class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        expression = ['+', '-', '*', '/']

        for token in tokens:
            if token in expression:
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    # be careful here
                    if b == 0:
                        return 0
                    if a*b < 0:
                        stack.append(-(abs(a)/abs(b)))
                    else:
                        stack.append(a/b)
                # print token, stack
            else:
                stack.append(int(token))
        # print stack
        return stack.pop(-1)



tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print Solution().evalRPN(tokens)
