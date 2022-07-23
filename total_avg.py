# Calculate total sum and Average
nums_list = [48, 45, 98, 12, 54, 65, 32, 78, 46]
sum = 0
avg = 0
for num in nums_list:
    sum = sum + num
    avg = sum / len(nums_list)

print("Number total sum is", sum)
print("Numbers average is", avg)