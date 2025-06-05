#isAlpha()
name = "PhyoMinKhant" #immutable
name_space = "Phyo Min Khant"
name_number = "PhyoMinKhant1"
result = name.isalpha()
result_of_space = name_space.isalpha()
result_of_number = name_number.isalpha()
print(f"Result of name: {result}")
print(f"Result of name_space : {result_of_space}")
print(f"Result of name_number : {result_of_number}")

#Capitalize()
name_for_capitalize = "phyo min khant"
result_capitalize = name_for_capitalize.capitalize()
print(f"Result of capitalize : {result_capitalize}")

#index()
result_index = name_space.index("Min")
print(f"Result of Index : {result_index}")

#Replace
result_replace = name_space.replace("Khant","Thant")
print(f"Result of Replace : {result_replace}")

#Center ---> Show in console
result_center = name.center(50)
print(result_center)