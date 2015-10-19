# This is the answer in the book LearningPython.
# Part Four,qusetion 3,4.

def adder(arg1,arg2):
	print('adder',end=' ')
	return arg1 + arg2

print(adder('Hello, ','World!'))
print(adder([1,2,3],[4,5,6]))
print(adder(1.2,2.8))

def adder1(*args):
	print('adder1',end=' ')
	if type(args[0])==type(0):
		sum = 0
	elif type(args[0])==type(dict()):
		sum = {}
		# print(type(sum))
	else:
		sum = args[0][:0]
	if type(args[0])==type(dict()):
		for arg in args:
		# 	print(sum)
		# 	print(arg)
			sum.update(arg)
	else:
		for arg in args:
			sum += arg
	return sum

def adder2(*args):
	print('adder2',end=' ')
	sum = args[0]
	if type(args[0])==type(dict()):
		for next in args[1:]:
			sum.update(next)
	else:
		for next in args[1:]:
			sum += next
	return sum

for func in (adder1,adder2):
	print(func(2,3,4))
	print(func('H','e','l','l','o'))
	print(func(['a','b'],['c','d'],['e','f'],'g'))
	print(func({'a':1,'b':2},{'c':3,'d':4}))

def adder3(good=1,bad=2,ugly=3):
	print('adder3',end=' ')
	return good + bad + ugly

print(adder3())
print(adder3(2,8))
print(adder3(2,4,5))
print(adder3(good=2,ugly=4))

def adder4(*args):
	print('adder4',end=' ')
	tot = args[0]
	for arg in args[1:]:
		tot += arg
	return tot

def adder5(**args):
	print('adder5',end=' ')
	argsKeys = list(args.keys())
	tot = args[argsKeys[0]]
	for key in argsKeys[1:]:
		tot += args[key]
	return tot

def adder6(**args):
	print('adder6',end=' ')
	argsValues = list(args.values())
	tot = argsValues[0]
	for value in argsValues[1:]:
		tot += value
	return tot

print(adder5(a=1,b=2,c=3))
print(adder5(a='aa',b='bb'))
print(adder6(a=1,b=2,c=3))
print(adder6(a='aa',b='bb'))
















