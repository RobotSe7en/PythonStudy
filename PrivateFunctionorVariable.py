def _private1(name):
	print('Hello, %s' % name)
def __private2(name):
	print('Hi, %s' % name)
def greeting(name):
	if len(name)>3:
		return _private1(name)
	else:
		return __private2(name)