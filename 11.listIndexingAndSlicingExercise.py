grades = [78,92,85,88,95,89]
third_student_grade = grades[2]
print(f" Third Student Grade : {third_student_grade}")
add_new_student_grade = grades.append(90)
print(grades)
grades_of_the_fist_three_students = grades[:3]
print(f"Grades of the first three students : {grades_of_the_fist_three_students}")

high_grades = [92,95,90]  
print(f"High Grades : {high_grades}")
rever_grades = grades[::-1]
print(f"Reverse Grade list : {rever_grades}")
every_other = grades[1:]
print(f"Every other : {every_other}")