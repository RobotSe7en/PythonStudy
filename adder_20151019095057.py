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
	elif type(args[0])==type({'a':1}):
		sum = {}
	else:
		sum = args[0][:0]
	if type(args[0])==type({'a':1}):
		for arg in args:
			sum = sum.update(arg)
	else:
		for arg in args:
			sum += arg
	return sum

def adder2(*args):
	print('adder2',end=' ')
	sum = args[0]
	for next in args[1:]:
		sum += next
	return sum

for func in (adder1,adder2):
	print(func(2,3,4))
	print(func('H','e','l','l','o'))
	print(func(['a','b'],['c','d'],['e','f'],'g'))
	print(func({'a':1,'b':2},{'c':3,'d':4}))