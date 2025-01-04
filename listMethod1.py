####### Appending ########
list = ["Aung Aung","Aung Aung","Mg Mg","Mya Mya","Phyo Phyo"]
print(f"Before appending : {list}")
after_append = list.append("Zaw Zaw")
print(f"After appending : {list}")

####### Poping #######
last_value = list.pop()
print(last_value)
print(list)

####### Counting #######
list = ["Aung Aung","Aung Aung","Mg Mg","Mya Mya","Phyo Phyo"]
count = list.count("Aung Aung")
print(f"How many Aung Aung include in list : {count}")

####### Inserting #######
list = ["Aung Aung","Aung Aung","Mg Mg","Mya Mya","Phyo Phyo"]
list.insert(0,"Ma Hla")
print(f" After inserting : {list}")

####### Removing #######
list = ["Aung Aung","Aung Aung","Mg Mg","Mya Mya","Phyo Phyo"]
list.remove("Aung Aung")
print(f"After removing : {list}")
