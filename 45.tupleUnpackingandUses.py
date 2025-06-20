#Tuple unpacking

# my_tuple = 1,2,3
my_tuple = (1,2,3)  #Tuple --> packing
num1,_,num3 = my_tuple  #Tuple --->Unpacking
print(num1)
print(num3)

#Value swapping
a = 12
b = 13
# c = a
# a = b
# b = c
# print(a)
# print(b)
a,b = b,a
print(a)
print(b)

numbers = [10,23,134,543,732,124,999]
def max_min_values(nums):
    return max(nums),min(nums)
min_value,max_value = max_min_values(numbers)
print(min_value)
print(max_value)


students = ['Aung Aung','Maung Maung','Mya Mya']
for index,name in enumerate(students):
    print(f"Student Id : {index}")
    print(f"Student Name : {name}")
