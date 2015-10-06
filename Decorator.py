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