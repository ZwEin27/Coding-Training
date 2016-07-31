import dateutil.parser as dparser

try:
    date = dparser.parse("")
except:
    print 'date'
else:
    print date
