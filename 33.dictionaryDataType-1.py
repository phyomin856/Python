#Dictionary Data Type
student_list = {"Bo Bo":"A" , "Min Min":"A+", "Kyaw Kyaw":"B+", "Mya Mya":"B-"}
first_student = student_list["Bo Bo"]
second_student = student_list["Min Min"]

#Adding new key-value
student_list["Aung Aung"] = "C"

#Modifying an existing value
student_list["Bo Bo"] = "D" #Mutable

#Removing a key-value
del student_list["Kyaw Kyaw"]
print(student_list)

