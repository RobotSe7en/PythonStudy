# Method1:
L1 = list(range(1,10))
print(L1)

# Method2: Struct [1x1,2x2,...,10x10]
L2 = []
for x in range(1,11):
	L2.append(x*x)
print(L2)

# Method3(ListComprehension): Struct [1x1,2x2,...,10x10]
L3 = [x*x for x in range(1,11)]
print(L3)

# Method4:
L4 = [m + n for m in ['A','B'] for n in ['X','Y']]
print(L4)

# Method5:
import os
L5 = [d for d in os.listdir('.')]

# Exercise
L = ['Hello', 'World', 18, 'Apple', None]
L6 = [s.lower() for s in L if isinstance(s,str)]
print(L6)