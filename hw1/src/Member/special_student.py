import math

from Member.student import Student

class Special_Student(Student):
	def __init__(self, name, score):
		self.name = name
		self.score = math.sqrt(score) * 10 
	def greet(self):
		print('Hi, I am a special_student')
