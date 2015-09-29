# factorial
def fact(n):
	if n == 1:
		return 1
	else:
		return fact(n-1)*n
print(fact(2))
print(fact(5))
# print(fact(100)) 会导致堆栈溢出

# # 针对堆栈溢出所做的优化
# def fact1(num,product):
# 	return fact_iter(n,1)

# def fact_iter(num,product):
# 	if num == 1:
# 		return product
#     return fact_iter(num-1,num*product)
# # fact_iter函数只返回函数本身(fact_iter)，并没有返回类似n*f(n)的形式

# Exercise:Hanoi
def hanoi(n,A,B,C):
	if n == 1:
		print(A,'==>',C)# 如果只有一个碟子，直接移动到C就可以
	else:
		hanoi(n-1,A,C,B)
		hanoi(1,A,B,C)
		hanoi(n-1,B,A,C)

hanoi(3,'A','B','C')
