nums = [2,4,6,8,10,12,14,16,18,20]
target = 12
left = 0
right = len(nums) - 1
found = False
while left <= right:
    mid = (right + left) // 2
    mid_value = nums[mid]
    if mid_value == target:
        print(f"Mid value found at index {mid_value}")
        found = True
        break
    elif mid_value < target:
        left = mid + 1
    else:
        right = mid - 1

if found == True:
    print(f"Target {target} found at index {mid}")


