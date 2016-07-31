import re
import string
# raw='http://milano.backpage.com/TranssexualEscorts/yana-shemale-ladyboy-39-3318914838-milan-corso-buenos-aires-11-17-201511-28-2015/3175352'

raw = 'Gargantita profunda y un exquisito trato de pareja! ?SHIRLEY? 0998130640 - 23 - 23 - Quito anuncios clasificados de escorts, modelos, edecanes, acompaantes - escorts - backpage.com 2016 06 17 - 21'
from datetime import datetime
def is_valid_datetime(raw, date_format):
    try:
        datetime.strptime(raw, date_format)
        return True
    except ValueError:
        return False

datetime_regexes = [
    r"(?:\d{2}[ _-]\d{2}[ _-]\d{4})",
    r"(?:\d{4}[ _-]\d{2}[ _-]\d{2})"
]
datetime_regex = r"(?:" + r"|".join(datetime_regexes) + ")"


re_digit = re.compile(r"\d+")
m = re.findall(datetime_regex, raw)
# print m
for d in m:
    # dd = d.translate(string.maketrans("",""), string.punctuation)
    # dd = ''.join(dd.split())
    dd = ''.join(re_digit.findall(d))
    print d
    print dd
    if is_valid_datetime(dd, '%Y%m%d') or is_valid_datetime(dd, '%m%d%Y'):
        print 'ss'
        raw = raw.replace(d, "")
print raw

raw = '2016 06 17'


# if m:
#     print m.group(1)
# else:
#     print 'no found'


# raw = re.sub(datetime_regex, '', raw, flags=re.I)
# print raw
