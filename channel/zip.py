import zipfile
import re

fmt = "{channel}.txt"
chan = 90052
comments = []

zf = zipfile.ZipFile('channel.zip', 'r')

while True:
	path = fmt.format(channel=chan)
	info = zf.getinfo(path)
	comments.append(info.comment)
	data = zf.read(path)
	match = re.search('[0-9]+', data)
	if match:
		chan = match.group(0)
	else:
		break;

print "".join(comments)

