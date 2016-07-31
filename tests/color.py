import re

text = 'white american'



reg_en_color = r'(?:\s*(white|black|yellow)\s*)'
re_en_color = re.compile(reg_en_color)
print re_en_color.sub('', text)
