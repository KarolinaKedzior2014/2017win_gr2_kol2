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

import json
from pprint import pprint

def add_student(students,name, age):
	students.append( { "Name" : name, "Age" : age, "Classes" : {} } )

def add_class(student, class_name):
	student['Classes'][class_name] = []

def get_student_class_attendance( student_classes, class_name):
	a = sum( [ class_lesson['Present'] for class_lesson in student_classes[class_name] ] )
	return 1.0 *a / ( 1.0* len(student_classes[class_name]))
def get_student_total_attendance(student):
	 return sum( get_student_class_attendance(student['Classes'], class_name) for class_name in student['Classes'] )*1.0 / (1.0 *len(student['Classes']) ) * 100.0

def get_avg_class_score( students, class_name):
	return sum( get_student_class_avg_score( student['Classes'], class_name) for student in students) / (1.0*len(students))

def get_student_class_avg_score( student_classes, class_name):
	a = sum( [class_lesson['Score'] for class_lesson in student_classes[class_name] ] )
	return  float(  a /len(student_classes[class_name])*1.0 )
	
def get_student_avg_score(student):
	 return float( sum( get_student_class_avg_score(student['Classes'], class_name) for class_name in student['Classes'] )
	 /len(student['Classes']) )
def get_total_avg_score(students):
	return float( sum( get_student_avg_score(student) for student in students )/len(students) )

import io, json
if __name__ == "__main__":
	data = None
	with io.open('students.json', 'r+', encoding='utf-8') as f:
		data = json.load(f)
		print("Avgerage score on PITE classes" ,get_avg_class_score( data['students'], "Math") )
		print("Avgerage score of Jan Kowalski, PITE classes (5): ", get_student_class_avg_score(data['students'][2]['Classes'], "PITE" ))
		print("Avgerage score of Anna Nowak", get_student_avg_score( data['students'][2] ))
		print("Avgerage score of all students: ", get_total_avg_score( data['students']) )
		print("Total student Adam Nowak attendance: ", get_student_total_attendance( data['students'][0]) )
		add_student(data['students'], "Bron Tan", 33)
		add_class(data['students'][3], "Math")
		f.seek(0)
		f.truncate()
		f.write(json.dumps(data, ensure_ascii=False))
		
	



	

