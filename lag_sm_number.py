# Find the Largest Number of a list
nums_list = [48, 45, 98, 12, 54, 65, 32, 78, 46]
largest = nums_list[0]
for num in nums_list:
    if num > largest:
        largest = num
print("Largest number you have is", largest)

# Find the Smallest Number of a list
nums_list = [48, 45, 98, 12, 54, 65, 32, 78, 46]
smallest = nums_list[0]
for num in nums_list:
    if num < smallest:
        smallest = num
print("Smallest number you have is", smallest)