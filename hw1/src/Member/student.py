from Member.base_member import Base_Member

class Student(Base_Member):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def greet(self):
		print('Hi, I am a student')
	def __str__(self):
		return 'Name: %s Score: %d' % (self.name, self.score)
