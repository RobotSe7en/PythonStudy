# Please creat lists with class Person, and sorted by name():
class  Person(object):
	pass

p1 = Person()
p1.name = 'Bart'
p2 = Person()
p2.name = 'Adam'
p3 = Person()
p3.name = 'Lisa'

L1 = [p1,p2,p3]
L2 = sorted(L1,key=lambda L1:L1.name)

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)

class Person1(object):
	"""docstring for Person1"""
	def __init__(self, name, gender, birth, **kw):
		self.name = name
		self.gender = gender
		self.birth = birth
		for key in kw.keys():
			setattr(self,key,kw[key])

xiaowang = Person1('xiaowang','male','33',job='teacher')
print(xiaowang.name,xiaowang.job)