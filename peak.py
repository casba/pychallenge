import pickle

data = pickle.load(open('banner.p', 'r'))

for d in data:
	print "".join( tup[0] * tup[1] for tup in d )
