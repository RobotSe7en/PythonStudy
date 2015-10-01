# filter函数用语过滤序列，和map类似，传入一个函数和一个序列，不同的是filter把传入的函数依次作用于每个元素，
# 然后根据返回值是True or False 决定保留还是丢弃这个元素
# Example1:
def is_odd(element):
	return element%2 == 1
print(list(filter(is_odd,list(range(1,11)))))

# Python 实现素数的筛选
# Firstly,define a odd sequence from 3.
def oddIter():
	n = 1
	while True:
		n = n + 2
		yield n
# Notice: This is a iterator
# Then define a selection function.
def notDivisible(n):
	return lambda x: x % n > 0
# Finally，define a iterator that can always return prime.
def prime():
	yield 2
	it = oddIter()
	while True:
		n = next(it)
		yield n
		it = filter(notDivisible(n),it)
# Test:
for n in prime():
	if n < 1000:
		print(n)
	else:
		break

# Exercise1:使用filter过滤掉非回数
def isPalindrome(n):
	return str(n) == str(n)[::-1]
print(list(filter(isPalindrome,range(1,1000))))
