import re

raw = '6474920245'

# re_dups = re.compile(r"\d{3}")
# rtn = re_dups.findall(raw)

def is_all_dup_digits(raw):
    for i in range(1, len(raw)/2):
        rtn = re.findall(r"\d{" + str(i) + r"}", raw)
        if len(raw) % i != 0:
            continue
        if all(rtn[0] == rest for rest in rtn):
            return True
    return False
print is_all_dup_digits(raw)
