# Exercise1:把用户输入的不规则名字按首字母大写，其他字母小写的规则修改
# Method1: Method with map.
def Normalize(name):
	return name[0].upper()+name[1:].lower()
L1 = ['adam','LISA','barT']
L2 = list(map(Normalize,L1))
print(L2)

# Method2: Method without map.
def Normalize1(name):
	res = []
	for n in name:
		res.append(n[0].upper() + n[1:].lower())
	return res

print(Normalize1(L1))

# Exercise2:编写一个prod函数利用reduce求给定的任意列表中元素的积
from functools import reduce
def Multipy(x,y):
	return x*y

def Prod(L):
	n = 1
	return reduce(Multipy,L)
L3 = [3,5,7,9]
print('3*5*7*9=',Prod(L3))

# Exercise3:利用map和reduce函数，把字符串'1234.567'转换成浮点数1234.567
def str2float(s):
	def char2num(s):
		lKey = (range(0,10))
		lvalue = range(0,10)
		d = dict(zip(map(str,lKey),lvalue))
		d['.'] = -1
		return d[s]
	point = 0
	def num2float(f,n):
		nonlocal point
		if n == -1:
			point = 1
			return f
		if point == 0:
			return f * 10 + n
		else:
			point = point * 10
			return f + n / point
	return reduce(num2float,map(char2num,s),0.0)
print(str2float('.111111'))

# 练习3的另一种解决办法，方法不错
def str2float(s):
	pop = s.find('.')
	floatLen = 10**(len(s) - pop - 1)
	s = s[:pop] + s[pop+1:]
	print (s)
	def num2int(x,y):
		return x*10 + y
	def char2num(s):
		lKey = (range(0,10))
		lvalue = range(0,10)
		d = dict(zip(map(str,lKey),lvalue))
		return d[s]
	return reduce(num2int,map(char2num,s))/floatLen
print(str2float('2222'))
		



