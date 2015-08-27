from Member.base_member import Base_Member

class Teacher(Base_Member):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def greet(self):
		print('Hi, I am a teacher')
	def __str__(self):
		return 'Name: %s Age: %s' % (self.name, self.age)
