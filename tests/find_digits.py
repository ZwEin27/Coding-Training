import re

# raw = 'tired 443 8235497 100hh 200 hour of the cnt games the girls that complain   well im not leaving until your sleeping in a 23423l2b23 cm stain       incalls $160 hh donation $260 hour donation outcalls start at $280 donation cat  409 4608923'

raw = "92535l4849.80"
re_ = re.compile(r'(?:\d{4,}[a-z]+\d{4,}\.)')
# raw = raw.replace(' ', '')
raw = re_.findall(raw)

print raw
