import re

data = open('equality.html', 'r').read()

match = re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', data)
print ''.join(match)
