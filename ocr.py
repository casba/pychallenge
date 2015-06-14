f = open('ocr.html', 'r')

s = f.read()

print ''.join(filter(str.isalpha, s))
