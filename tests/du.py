import re
text = '10days'
re_ = re.compile(r'^\d+?\s*?(?:second|minute|hour|day|week|year)s?$')

print re_.findall(text)
