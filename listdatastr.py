myInfo = ["Phyo Min Khant","180cm",22,"Student",["Algorithm and Data Structure","Human Computer Interaction and Web Development"]]
Size = len(myInfo)
print(f"Size is {Size}")
print(type(Size))
print(type(myInfo))
name = myInfo[0]
sub = myInfo[4]
myInfo[1] = "181cm"
height = myInfo[1]
print(myInfo)
myInfo.append("Myanmar")
Nationality = myInfo[-1]
print(myInfo)

print(f"My name is {name} and I was taking 2 subjects that are {sub} and my height is {height}. I am {Nationality}.")