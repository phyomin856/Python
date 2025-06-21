#Union
#Interset
#Difference


#Union
phone_contact = {"Aye Aye","Mya Mya","Kyaw Kyaw","Min Min"}
email_contact = {"Aye Aye","Bo Min","Min Khant"}
all_contact = phone_contact.union(email_contact)
print(all_contact)

#Interset
my_interest = {"Dancing","Music","Coding","Swimming"}
friend_interest = {"Dancing","Coding","Cooking","Listening"}
common_interest = my_interest.intersection(friend_interest)
print(common_interest)

#Difference
my_task = {"Task1","Task2","Task3","Task4"}
complete_task = {"Task1","Task2"}
need_to_do_task = my_task.difference(complete_task)
print(need_to_do_task)