students = ["Maung Maung","Aung Aung","Mya Mya","Zaw Zaw","Zaw Zaw"]
print(f"Before appending of students : {students}")
appending = students.append("Ko Ko")
print(f"After appending of students : {students}")
pop = students.pop()
print(f"After popping of students : {students}")
print(f"Popping : {pop}")
count = students.count("Zaw Zaw")
print(f"Counting : {count}")
insert = students.insert(0,"Phyo Phyo")
print(f"After inserting : {students}")
remove = students.remove("Zaw Zaw")
print(f"After removing in students : {students}")
print(remove)