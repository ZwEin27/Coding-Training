import re

text = '36 40 DD'



reg_breast = r'(?:\w+)'
re_breast = re.compile(reg_breast)
print re_breast.findall(text)
