# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
  
total_height = sum(student_heights)
number_of_student = int(len(student_heights))
average = round(int(total_height)/number_of_student)
print(f"total height = {total_height}")
print(f"number of students = {number_of_student}")
print(f"average height = {average}")