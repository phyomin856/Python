#String Indexing and String Slicing

#String Indexing
name = "Technortal"
print(name[1])
print(name[2])
print(name[-1])

#String Slicing
print(name[0:4]) # [Start : End(exclusive) : Step]
print(name[0:8:1])
print(name[0:8:2]) #answer --> Tcnr because of Step(2)

#Copy
copy_of_index = name[:]
print(copy_of_index)

#Reverse Copy
reverse_copy_of_index = name[::-1]
print(reverse_copy_of_index)