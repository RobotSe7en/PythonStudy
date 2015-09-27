# generator:While loop calculation(Saving Spaces)
# A example of not generator:
L1 = [x*x for x in range(1,10)]
print(L1)

# A example of generator:
L2 = (x*x for x in range(1,10))
print(L2)
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
print(next(L2))
#print(next(L2)) # Exceed L2(print an erro)

# Fibonacci sequence
def fib1(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b = b,a + b
		n = n + 1
	return 'done'

fib1(10)
# The output is a list,not a generator.

def fib2(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a + b
		n = n + 1
	
print(fib2(10))
# The output is a generator.



