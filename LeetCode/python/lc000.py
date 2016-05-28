# Test part

# test = {
#     '1': '0.1',
#     '2': '0.2'
# }
# test = sorted(test.iteritems(), key=lambda x: x[1], reverse=True)
# test = [int(_[0]) for _ in test]
#
# # tmp = test.get(1)
# # tmp.extend([4,5,6])
# print test

# x = [4,2,4,5,3,7]
# for cur, val in enumerate(x):
#     print cur, val

import numpy as np

# print np.random.randint(2, size=1)

# tmp = np.random.random_integers(0, 1, size=2)
# print tmp
# print np.where(tmp)
# print np.random.random_integers(0, 1, size=2)

# size = 100
# tmp = np.arange(size)
# np.random.shuffle(tmp)
# print tmp[:int(size*.1)]

# l = [2,2,2]
# print l.index(2)
# from decimal import Decimal
# print '%.e' % Decimal('0.00001')
# import os
# path = '/Users/ZwEin/job_works/StudentWork_USC-ISI/projects/WEDC/tests/data/san-francisco-maria-2.json'
# drive, path_and_file = os.path.splitdrive(path)
# path, file = os.path.split(path_and_file)
# print path
# print file


# import json
# json.dumps([{'bar': ('baz', None, 1.0, 2)}])

t = (123, '111')
k, v = t
print k
print v
