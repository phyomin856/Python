#conditional statement
area = 5 * 8 

#conditional expression
#value_if_true #if #condition #value_if_false 
x = 6
result = "positive" if x > 4 else "false"
print(result)

member_type = "Gold"
discount_rate = 0.3 if member_type == "Gold" else 0.1
price = 100
actual_price = price - (discount_rate * price)
print(f"Actual Price is : {actual_price}")

memberType = "Bronze"
discount = 0.1 if memberType == "Sliver" else 0.05
Price = 100
actualPrice = Price * (1-discount)
print(f"Actual Price : {actualPrice}")