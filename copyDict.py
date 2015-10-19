# This is the answer in book LearningPython
# Part Four,question 4,6.

def copyDict(old):
	new = {}
	for key in old.keys():
		new[key] = old[key]
	return new

d = {'a':1,'b':2,'c':3}
e = copyDict(d)
print(e)
d = {'a':1,'b':2,'c':5}
print(e)

def addDict(d1,d2):
	new = {}
	for key1 in d1.keys():
		new[key1] = d1[key1]
	for key2 in d2.keys():
		new[key2] = d2[key2]
	return new

print(addDict({1:2,3:4},{5:6,7:8}))