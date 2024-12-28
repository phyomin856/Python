##### Using print function by using format method and format string #####

name = "Phyo Min Khant"
job = "Student"

##### Format Method #####
print("My name is {} and I am a {}".format(name,job))
print("My name is {1} and I am a {0}".format(name,job))

##### Format String #####
print(f"My name is {name} and I am a {job}.")

Name = "Phyo Min Khant"
Job = "Student"
age = 22
print(f"My name is {Name} and I am a {Job} and {age} years old.")
print("My name is {} and I am a {} and {} years old.".format(Name,Job,age))