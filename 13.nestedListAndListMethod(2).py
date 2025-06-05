students = ["Aung Aung","Mya Mya","Kyaw Kyaw",["Khant Khant","Daw Daw"]] #nested list
print(len(students))
print(students[3])
print(students[3][1])
print(students.clear())
print(f" After clearing of students : {students}")

old_num = [1,2,3,4]
coppied_num = old_num.copy()
print(coppied_num)

print(old_num.index(3))

new_num = [5,6,7,8]

old_num.extend(new_num)
print(old_num)

nums = [3,5,32,4,7,6]
nums.sort()
print(nums)

nums_reversed = [2,5,3,1,4,8,6]
nums_reversed.sort(reverse=True)
print(nums_reversed)
nums_reversed.reverse()
print(nums_reversed)