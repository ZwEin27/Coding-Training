import re
# raw = 'helel hele1ghthell e1ght'
#
# raw = raw.replace('e1ght', 'eight')
#
# print raw

raw = 'hello twenty_1 twotwenty-two'

# re_ = re.compile(r"(.*)(twenty[\W_]{0,3})(\d)(.*)")
# raw = re_.sub("2", raw)


# raw = re.sub(r"(.*)(twenty[\W_]{0,3})(\d)(.*)", r"\g<1>2\g<3>\g<4>", raw, flags=re.I)
re_ = re.compile(r"(two|twenty[\W_]+(?=(\d|zero|one|two|three|four)))")
raw = re_.sub('2', raw)


print raw
