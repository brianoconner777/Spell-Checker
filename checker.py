import re , collections



a = file('train.txt').read()

b = words(a)

def words(txt):
 return re.findall('[a-z]+',text.lower())

def train(t):
	has = collections.defaultdict(lambda : 1)
	for f in t:
		has[f] += 1
	return has


