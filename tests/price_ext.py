import re
import inflection

time_units = [
    'half',
    'half hr'
    'half hour',
    'hlf hr',
    'hlf hour',
    'h hr',
    'h hour',
    'hh',
    'hhr',
    'h',
    'hr',
    'hour',
    'hourly',
    'fh',
    'q',
    'qk',
    'qv',
    'hummer',
    'min',
    'minute',
    'ss',
    'second'
]

price_units = [
    '\$',
    'dollar',
    'euro',
    'nuck',
    'rose',
    'candy',
    'donation'
]

# raw = 'tired 443 8235497 100hh 200 hour of the cnt games the girls that complain   well im not leaving until your sleeping in a 23423l2b23 cm stain       incalls $160 hh donation $260 hour donation outcalls start at $280 donation cat  409 4608923'

# raw = "15 min $50 half hr $70 full hr $100 call  "
raw = "bodywork $50 hr $65hr original table shower body scrub bodywork $60 hr before 3pm 4 hand special $99 hr including free table shower call "

# re_ = re.compile(r'(?:\$?\d+[a-z ]+)')
reg_price_time_digit = r'\d{1,4}'
reg_price_time_interval = r'\w{,10}'
reg_price_time_price_units = r'(?:'+ r'|'.join(price_units) + r')?'
reg_price_time = r'(?:' + \
        reg_price_time_price_units + \
        reg_price_time_digit + \
        reg_price_time_price_units + \
        r'[\t ]?' + \
        r'(?:'+ r'|'.join(time_units) + r')' + \
        ')'
re_price_time = re.compile(reg_price_time)
# raw = raw.replace(' ', '')
raw = re_price_time.findall(raw)

print raw
