#nested If 
temperature = 30
day_of_time = "night"

if temperature >= 30:
    if day_of_time == "morning":
        print("It's hot in the morning")
    elif day_of_time == "afternoon":
        print("It's hot in the afternoon")
    else:
        print("It's hot in the night")
else:
    print("The temperature is not too high")