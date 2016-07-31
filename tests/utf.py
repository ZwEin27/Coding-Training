ll = ['\\u200b', '', '', '', '\\u200b', '', '\\u200b', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\\u200b', '', '\\u200b', '\\u200b', '', '', '', '', '', '', '\\u200b', '', '\\u200b', '', '', '\\u200b', '\\u200b', '', '\\u200b', '', '', '', '\\u200b', '', '', '\\u200b', '', '\\u200b', '\\u200b', '']

import re

re_de_unicode = re.compile(r'\\+u.*?\b')

for l in ll:
    l = re_unicode.sub('', l)
    print 'a'+ l+ 'a'
    # print l.encode('ascii', 'ignore')
