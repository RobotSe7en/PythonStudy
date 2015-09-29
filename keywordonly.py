def kwonly(a,*b,c):
	print(a,b,c)

kwonly(1,2,c=3)
kwonly(a=1,c=3)
# kwonly(1,2,3)
kwonly(1,2,3,4,c=5)
kwonly(1,*[2,3,4],c=5) # when call function with asterisk before a args,the agrs will be unpack.

def kwonly2(a,*,b,c):
	print(a,b,c)
# This function will allow deliver a list type，but can not be unpacked.
kwonly2(1,b=2,c=5)
# kwonly2(1,*[2,3,4],c=5)

def kwonly3(a,*,b='spam',c='ham'):
	print(a,b,c)
kwonly3(1)
kwonly3(1,b=2)
# 带有默认值的keyword－only参数是可选的，但是没有默认值的keyword－only参数必须要传入值

# Search common argument and return these arguments.
def intersect(*args):
	res = []
	for x in args[0]:
		for other in args[1:]:
			if not x in other:
				break
			else:
				res.append(x)
	return res

# Record arguments that was visited
def union(*args):
	res = []
	for seq in args:
		for x in seq:
			if not x in res:
				res.append(x)
	return res

s1,s2,s3 = 'spam','scam','slam'
print(intersect(s1,s2),union(s1,s2))







