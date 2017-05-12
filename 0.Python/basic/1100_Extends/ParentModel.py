class Parent(object):
	"""docstring for Parent"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('Parent has been inited!')

	def introduce(self):
		print('My name is',self.name,'I am',self.age,'years old')

if __name__ == '__main__':
	parent = Parent('parent','29')
	parent.introduce()