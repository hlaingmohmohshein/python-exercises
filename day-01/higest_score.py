# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    max = student_scores[0]
    if max < student_scores[n]:
        max= student_scores[n]
# Write your code below this row 👇
print(max)