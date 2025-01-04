####### Clear #######
list = [4,2,6,8,10,11,18,29,40]
print(f"Before Clear list : {list}")
list.clear()
print(f"After Clear list : {list}")

####### Copy #######
list = [4,2,6,8,10,11,18,29,40]
print(f"Before Copy list : {list}")
new_list = list.copy()
print(f"After Copy list : {new_list}")

####### Index #######
list = [4,2,6,8,10,11,18,29,40]
searchIndex = list.index(10)
print(f"Index number of 10 is : {searchIndex}")

####### Extend #######
oldStudent = ["Aung Aung","Mg Mg","Mya Mya"]
newStudent = ["Hla Hla","Hein Hein"]
oldStudent.extend(newStudent)
print(f"All of students are : {oldStudent}")

####### Sort #######
data = [40,50,20,90,1,30,9,5]
data.sort()
print(f"After Sorting : {data}")
data.sort(reverse=True)
print(data)

####### Reverse #######
list = [4,2,6,8,10,11,18,29,40]
list.reverse()
print(f"After using reverse : {list}")