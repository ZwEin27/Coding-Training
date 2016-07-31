
text = 'Reviewed #229512 T e R'

import re

re_ = re.compile(r'(?:\bt\s*?[e3]?\s*?r|\bt\s*?[e3]|\b[e3]\s*?p|\bt\b|\be\b|\br\b)', re.IGNORECASE)

print re_.findall(text)
