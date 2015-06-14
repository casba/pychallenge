def rot(x):
	nch = ord(x)+2;
	lo = 'a'
	hi = 'z'
	if ( ord(x) >= ord('a') and ord(x) <= ord('z')):
		lo = 'a'
		hi = 'z'
	elif ( ord(x) >= ord('A') and ord(x) <= ord('Z') ):
		lo = 'A'
		hi = 'Z'
	else:
		return x

	if ( nch > ord(hi) ):
		nch = (ord('a') + (nch-ord(hi)))-1
	
	return chr(nch)

encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decoded = ''.join(map(rot, encoded))
print ''.join(map(rot, "map"))
print decoded;
