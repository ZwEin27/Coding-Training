# raw = '&raquo; United States &raquo; North Carolina &raquo; Rocky Mount &raquo;'
# import re
# # re_ = re.compile(r'&[a-zA-Z]+?;')
# re_ = re.compile(r'&\w+?;')
# raw = re_.sub('', raw)
# # raw = raw.replace(/<<|>>/g, '')
# print raw

import re
print re.split(r'[, ]', 'los angeles, california')
