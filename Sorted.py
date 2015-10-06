# sorted函数可以对列表进行由小到大的排序，也可以传入一个函数
print(sorted([1,-4,2,3,-5],key=abs))
# 传入一个函数，对传入的列表的每一个元素都进行调用abs函数，根据作用之后的元素进行由小到大排序
# Exercise：假设用一个元组(tuple)表示一个班级的姓名及对应的成绩，按照姓名进行排序
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def byName(t): # Sorted by name
	return t[0]

def byScore(t):
	return t[1]

print(sorted(L,key=byName,reverse=False))
print(sorted(L,key=byScore,reverse=True))