import re

fmt = "{channel}.txt"
chan = 90052

while True:
	path = fmt.format(channel=chan)
	print 'searching in: ', path
	data = open(path, 'r').read()
	match = re.search('[0-9]+', data)
	if match:
		chan = match.group(0)
	else:
		print data
		break;
