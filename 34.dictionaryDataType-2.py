#Methods
student_list = {"Ko Ko": 99, "Phyo Phyo": 100, "Mya Mya": 78, "Kyaw Kyaw": 88}

#Key
# for sl in student_list.keys():
#     print(student_list[sl])
print(student_list.keys())

#Value
# print(student_list.values())
print(student_list.values())

#item
print(f"This is tuple : {student_list.items()}") #tuple [('Phyo Phyo' : 100)]

#get
# print(student_list["Aye Aye"]) #ma shi tk key ko access lok yin key error tet
print(student_list.get('Aye Aye')) #--> show None

#Pop
grade = student_list.pop("Ko Ko")
print(grade)
print(student_list)

#Popitem
print(student_list.popitem())
print(student_list)
