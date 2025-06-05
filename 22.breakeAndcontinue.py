students = ['AungAung','MaungMaung','MyaMya','AyeAye','BoBo','PhyoPhyo','MinMin','KhantKhant']
choose_student = 'AyeAye'
index = 0
while index < len(students):
    if choose_student == students[index]:
        print("Student Found")
        # break
       
    else:
        print("Student Not found")
    index += 1
    # continue