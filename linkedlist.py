import requests
import re

url_temp = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
chain = 16044/2

cnt = 0
while cnt < 400: #page says more than 400 not necessary
	print 'requesting ', url_temp.format(nothing=chain)
	r = requests.get(url_temp.format(nothing=chain))
	if r.status_code != 200:
		print 'Error this request failed'
		break;

	match = re.search('and[^0-9]*([0-9]+)', r.text)
	if match:
		chain = match.group(1)
	else:
		print chain, r.text
		break;
	cnt = cnt+1


