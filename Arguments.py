# default argument's trap.
def add_end(L=[]):
	L.append('end')
	return L
print(add_end())
print(add_end())
print(add_end())
# The function remembered last list which added 'end'.
# To solve this problems,define function as follows:
def add_end_Recorrected(L=None):
	if L is None:
		L = []
	L.append('end')
	return L
print(add_end_Recorrected())
print(add_end_Recorrected())
print(add_end_Recorrected())

# Varargs
# Method1:
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc([1,2,3,4]))
print(calc((1,2,3,4)))

# Method2: Args were composed into a tuple.
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc2(1,2,3,4))
print(calc2(*[1,2,3,4])) # When we call a function with asterisk before a list,this list will be unpacked.









