#nested Function 
def greet():  #enclosed Function
    print("Hello")
    name = "Phyo Min Khant"
    def introduction(): #nested Function                    #local scope
        print(f"My name is {name} ")                        #local scope
    introduction()
    print(name)
greet()
