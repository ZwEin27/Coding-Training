import re

raw = "i m very upscale and discreet all of my services are unrushed and satisfying i m available all nite so don t hesitate 2 contact me please contact me when you re ready 2 be seen couples welcomed 7 0 8 8 8 0 9 2 9 6 708 8 8 0 9296 holly 708 8 8 0 9296."
phone_number_format_regex = [
    r"(?:" + 10*r"[ ]\d" + r")", #
    r"(?:[ ]?\d{10}[ ])",
    r"(?:[ ]?\d{8}[ ]\d{3}[ ]?)",
    r"(?:[ ]?\d{7}[ ]\d{4}[ ]?)",
    r"(?:[ ]?\d{4}[ ]\d{4}[ ]\d{2}[ ]?)",
    r"(?:[ ]?\d{3}[ ]\d{7,8}[ ]?)",
    r"(?:[ ]?\d{3}[ ]\d{3}[ ]\d{4}[ ]?)",
    r"(?:[ ]?\d{3}[ ]\d{3}[ ]\d{1}[ ]\d{3}[ ]?)",
    r"(?:[ ]?\d{2}[ ]\d{4}[ ]\d{4}[ ]?)",
    r"(?:[\d ]{20,22})",
    r"[\d ]+"
]
numbers_regex = r"(?:" + r"|".join(phone_number_format_regex) + r")"
print re.findall(numbers_regex, raw)
# print re.findall(r"(?:\d[ ]\d[ ]\d[ ]\d[ ]\d[ ]\d[ ])", raw)
