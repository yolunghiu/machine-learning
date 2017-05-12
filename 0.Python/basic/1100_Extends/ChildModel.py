import ParentModel
class Child(ParentModel.Parent):
	"""docstring for Parent"""
	# 如果子类不重写init方法，则子类会继承父类的属性
	def __init__(self, name, age, salary):
		ParentModel.Parent.__init__(self, name, age)
		self.salary = salary
		print('Child has been inited!')

	def introduce(self):
		ParentModel.Parent.introduce(self)
		print('My salary is ', self.salary)
if __name__ == '__main__':
	child = Child('child','19', '100000')
	child.introduce()