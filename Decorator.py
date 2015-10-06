# Because function is an object, and an argument can get a function,
# so we can call a function by an argument
def now():
	print('2015-10-06')

f = now
f()
# Function has property(__name__) that can get the function's name
# For example:
print(now.__name__)
print(f.__name__)
print('================')
# Now we want to enchance now() function,such as printing a lauching log before call it,
# but we do not want to remodify now(),the way to add function during code is running 
# is called decorator.
# Essentially,decorator is a high-oder function which return a function.
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
# 函数中wrapper()中的参数定义是用来传递now1的参数的(若没有，就不传入)
@log
def now1(s):
	print(s)
now1([1,2,3,4])
print('================')
# Exercise1:
print('Exercise1:')
def log1(func):
	def wrapper1(*args,**kw):
		print('begin call')
		func(*args,**kw)
		print('end call')
	return wrapper1

@log1
def now2(s):
	print(s)
now2('WTF')

print('================')
# help(hasattr)
# Exercise2:
def log2(arg):
	text = 'call' if hasattr(arg,'__call__') else arg
	def decorator(func):
		def wrappper2(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrappper2
	return decorator(arg) if hasattr(arg,'__call__') else decorator

# @log2('execute')
@log2
def now3(s):
	print(s)

now3('Sucess')