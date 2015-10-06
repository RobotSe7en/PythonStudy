# lazySum
def lazySum(*args):
	def sum():
		sumCache = 0
		for i in args:
			sumCache = sumCache + i
		return sumCache
	return sum
f = lazySum(*[1,2,3,4])
print(f())
# 在第9行，我们调用lazySum时，并没有求和，而是直接返回一个函数，再一次调用f时才真正的返回结果
# Attention：每次调用lazySum时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazySum(2,3,4)
f2 = lazySum(2,3,4)
print(f1 == f2)

