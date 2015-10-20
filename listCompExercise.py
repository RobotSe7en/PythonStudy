# This is the answer in the book LearningPython
# Part Four,question 9.

from math import sqrt
L = [2,4,9,16,25]
res = []
for l in L:
	res.append(sqrt(l))
print(res)
print(list(map(lambda l:sqrt(l),L)))
print([sqrt(l) for l in L])