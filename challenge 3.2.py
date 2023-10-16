class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(students_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(students_list, key=lambda students: students.cgpa, reverse=True)
  return sorted_students


#Example usage:
students = [
  student("Divya", "A123", 8.9),
  student("sandhiya", "A124", 9.2),
  student("Buvana", "A125", 7.5),
  student("Gokul", "A126", 9.5),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("name: {}, roll number: {}, CGPA: {}". format(student.name, student.roll_number, student.cgpa))