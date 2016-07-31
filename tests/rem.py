import re

raw = 'two62'

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'siz', 'seven', 'eight', 'nine']
re_twenty_x = re.compile(r"(two|twenty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")

raw = re_twenty_x.sub('', raw)
print raw
