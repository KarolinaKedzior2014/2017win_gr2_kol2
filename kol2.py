# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
import sys
import math
import random

class StudentOrganizer:
	def __init__(self, list_of_students):
		self.students = list_of_students
	def get_avg_class_score(self, class_name):
		avg = 0.0
		i = 0
		for student in self.students:
			if student.class_name == class_name:
				avg = avg + student.score
				i = i+1
		return float(avg/i)
	def get_total_avg_score(self):
		avg = 0.0
		i = 0
		for student in self.students:
			avg = avg + sum(student.scores)			
			i = i+ 1
		return float(avg/i)

	
class Student:
	def __init__(self,name, surname, class_name):
		self.name = name
		self.surname = surname
		self.class_name = class_name
		self.scores = []
		self.attendance = { }
	def add_score(self, new_score):
		self.scores.append(new_score)
	def set_if_present(self, date, is_present):
		self.attendance[date] = is_present


if __name__ == "__main__":
	my_students_list = [Student( "Tom" , "A" , "1A"),Student( "Tom" , "w" , "1A"),Student( "Tom" , "A" , "1B"), Student( "Tom" , "e" , "1B"),Student( "Tom" , "D" , "1B"),Student( "Tom" , "C" , "1C"),Student( "Tom" , "b" , "1C")]
	for student in my_students_list:
		student.add_score( random.randint(2,6) )
		student.set_if_present( "11.11.2017",  random.randint(0,2) )
	student_organizer = StudentOrganizer(my_students_list)
	print ("Student total average" , student_organizer.get_total_avg_score() )
	



	

