#Arges and Kwargs
def area(*arges):
    print(arges)
area(1,3,4,2,2,33,5643,322)

def test(*tes):
    for i in tes:
        print(i)
test(12,44,63,266,854,22)

def student(**kwargs):
    print(kwargs)
student(name = "Phyo Min Khant",age = '22', Township = "Mandalay")

def func(num,*nums):  #func(*nums,num) ---> error
    print(num)
    print(nums)
func(1,343,21,46,447,885,43)

def log_message(level,*messages,**details):
    print(f"Log Level : {level}")
    for message in messages:
        print(f"Message : {message}")
    for key,values in details.items():
        print(f"{key}:{values}")
log_message("INFO","User Logged in","Action : View Dashboard",user_id = 111,ip_address = '192.10.0.1')