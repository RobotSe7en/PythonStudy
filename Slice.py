L = ['Micheal','Sarah','Tracy','Bob','Jack']
# Method1:
L_cache = [L[0],L[1],L[2]]
print(L_cache)

# Method2(Slice n elements):
L_cache2 = []
n = 0
while n<3:
	L_cache2.append(L[n])
	n = n + 1
print(L_cache2)

# Method3(Simple method):
L_cache3 = L[0:3]
print(L_cache3)