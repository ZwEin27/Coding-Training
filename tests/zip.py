
RES_HAIR_COLOR_LEVEL = [
    'Light',
    'Dark'
]

RES_HAIR_COLOR = [
    'Blond',
    'Blonde',
    'Red',
    'Brown',
    'Black',
    'Grey',
    'White',
    'Brunet',
    'Brunette'
]
import itertools
# for i, j in itertools.product(RES_HAIR_COLOR_LEVEL, RES_HAIR_COLOR):
#     print i, j

print [' '.join([i, j]) for i, j in itertools.product(RES_HAIR_COLOR_LEVEL, RES_HAIR_COLOR)]
