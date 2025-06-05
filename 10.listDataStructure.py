students = ["Maung Maung","Aung Aung","Mya Mya","Kyaw Kyaw"]
first_student = students[0]
print(f"First student : {first_student}")

#Mutable
print(f"Before change sec student : {students}")

students[1] = "Phyo Phyo"
print(f"After change sec student : {students}")

#Dynamic Size
list = [1,"hello","Phyo Min Khant",["Myanmar","English","Math"],1.23,True]
print(f"Before list appending : {list}")
list.append(False)
print(f"Result of appending list : {list}")

