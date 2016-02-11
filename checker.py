import re , collections



a = file('train.txt').read()

b = words(a)

def words(txt): return re.findall('[a-z]+',text.lower())

