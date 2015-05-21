import sys

from Member.base_member import Base_Member
from Member.teacher import Teacher 
from Member.student import Student
from Member.special_student import Special_Student

def main(argv):
	members = dict()
	while True:
		try:
			input_string = input()
			input_string = input_string.replace("\r", "")
			split_list = input_string.split(" ")
			if split_list[0] == 'add':
				if split_list[1] == 'teacher':
					members[split_list[2]] = Teacher(split_list[2], int(split_list[3]))
				if split_list[1] == 'student':
					members[split_list[2]] = Student(split_list[2], int(split_list[3]))
				if split_list[1] == 'special_student':
					members[split_list[2]] = Special_Student(split_list[2], int(split_list[3]))
			if split_list[0] == 'greet':
				members[split_list[1]].greet()
			if split_list[0] == 'remove':
				del members[split_list[1]]
			if split_list[0] == 'show':
				for i in iter(members):
					print(members[i])
		except EOFError:
			break

if __name__ == '__main__':
	    sys.exit(main(sys.argv))
