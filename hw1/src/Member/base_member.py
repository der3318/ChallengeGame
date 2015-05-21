class Base_Member():
	def __init__(self, name):
		self.name = name
	def greet(self):
		print('Hi, I am a member')
	def __str__(self):
		return 'Name: %s' % self.name
