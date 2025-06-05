# nums = [1,3,4,5,68,2,4,6]
# target_num = 68
# for num in nums:
#     if target_num == num:
#         print(f"Target Number {target_num} was found")
#     else:
#         print("Not found")

nums = [1,3,4,5,68,2,4,6]
flag = False
target_num = 58
for i in range(len(nums)):
    if target_num == nums[i]:
        print(f"Target Number {target_num} was found at index {i}")
        flag = True
        break
if flag == False:
    print("not found")