text = "Phyo Min Khant Aung Khant Phyo Phyo Min Khant"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

student = {
        "Name":"Phyo Min Khant",
        "Age" : 22,
        "Grades":{
            "Myanmar":66,        #nested dictionary
            "Eng":43,
            "Math":84
        } 
           }
print(student)

Library = {
    "Fiction" : ["Myanamr","Eng","Math"],
    "Non-fiction" : [],
    "Science" : []
}